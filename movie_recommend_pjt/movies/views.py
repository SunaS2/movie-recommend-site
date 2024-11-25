from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Movie, Genre, Ott, Comment, CommentLike, WishMovieHistory
from voca_notes.models import VocaNote
from .serializers import (
    MovieListSerializers,
    WishMovieSerializer,
    OttListSerializers,
    GenreListSerializers,
)
from .serializers import (
    CommentSerializer,
    CommentListSerializer,
    CommentUserListSerializer,
    WishMovieVocaSerializer,
    RandomMovieSerializer,
)
from .serializers import CommentUserLikedSerializer
import random


User = get_user_model()


# 영화 전체 조회
@api_view(["GET"])
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializers(movies, many=True, context={"request": request})
    return Response(serializer.data)


# 영화 좋아요 눌렀을 때 내 프로필 페이지에서 wish_movies 볼 수 있게 vue에서 버튼 누르면 저장시키는 로직
@api_view(["POST"])
def wish_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    if movie.wish_users.filter(id=user.id).exists():
        # 이미 좋아요를 눌렀으면 취소
        movie.wish_users.remove(user)
        return Response(
            {"status": "removed", "movie_pk": movie_pk}, status=status.HTTP_200_OK
        )
    else:
        if not WishMovieHistory.objects.filter(user=user, movie=movie).exists():
            # 경험치 추가
            user.experience += 30
            user.save()
            WishMovieHistory.objects.create(user=user, movie=movie)

        # 좋아요 추가
        movie.wish_users.add(user)
        return Response(
            {"status": "added", "movie_pk": movie_pk}, status=status.HTTP_200_OK
        )


# 로그인 유저 난이도별 추천 영화 랜덤 5개
@api_view(["GET"])
def random_recommend_movie(request):
    login_user = request.user
    user_study_level = login_user.study_level
    movies = Movie.objects.filter(difficulty=user_study_level)

    recommended_movies = random.sample(list(movies), min(5, len(movies)))

    serializer = RandomMovieSerializer(recommended_movies, many=True)
    return Response(serializer.data, status=200)


# 로그인 한 유저가 좋아요 한 영화 목록
@api_view(["GET"])
def logined_wish_movie_list(request):
    login_user = request.user
    wished_movies = Movie.objects.filter(wish_users=login_user)

    serializer = WishMovieSerializer(
        wished_movies, many=True, context={"request": request}
    )
    return Response(serializer.data)


# 로그인 한 유저의 wish movies중 vocanote 없는 리스트 목록
@api_view(["GET"])
def wish_movie_without_vocanote(request):
    login_user = request.user

    wished_movies = Movie.objects.filter(wish_users=login_user)

    # voca_notes가 없는 영화만 필터링 (빈 리스트나 연결된 voca_note가 없으면 Count가 0)
    without_vocanote_movies = wished_movies.annotate(
        voca_note_count=Count("voca_notes")
    ).filter(voca_note_count=0)
    serializer = WishMovieVocaSerializer(without_vocanote_movies, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def genres_list(request):
    genres = Genre.objects.all()
    serializer = GenreListSerializers(genres, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def otts_list(request):
    otts = Ott.objects.all()
    serializer = OttListSerializers(otts, many=True)
    return Response(serializer.data)


# 코멘트 생성
@api_view(["POST"])
def comment_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # movies, users iterable이기 때문에 단일 객체 리스트 형태로[]로 감싸줘야함
            serializer.save(movies=[movie], users=[request.user])
            serializer.save()

            request.user.experience += 20
            request.user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 유저가 작성한 comment 조회
@api_view(["GET"])
def comment_list_user(request):
    login_user = request.user

    if request.method == "GET":
        # 유저가 작성한 모든 영화에 따른 코멘트 내용들
        comments = Comment.objects.filter(users=login_user)
        serializer = CommentUserListSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 영화별 코멘트 조회
@api_view(["GET"])
def comment_list_movie(request, movie_pk):

    movie = Movie.objects.get(pk=movie_pk)

    if request.method == "GET":
        comments = Comment.objects.filter(movies=movie)
        serializer = CommentListSerializer(comments, many=True)

        # 해당 영화에 대한 총 코멘트 수
        total_comments = comments.count()

        return Response(
            {
                "number_of_count": total_comments,  # 총 코멘트 개수
                "comments": serializer.data,  # 코멘트 목록
            },
            status=status.HTTP_200_OK,
        )


@api_view(["DELETE"])
def comment_delete(request, comment_pk):
    login_user = request.user
    comment = get_object_or_404(Comment, pk=comment_pk, users=login_user)

    # 삭제 전에 필요한 정보 저장
    comment_id = comment.pk
    comment_content = comment.content
    comment.delete()

    return Response(
        {
            "message": f"Comment with ID {comment_id} has been deleted.",
            "deleted_content": comment_content,
        },
        status=status.HTTP_200_OK,
    )


# 코멘트 수정 => 현재 로그인한 유저만 수정 권한 있음.
@api_view(["PUT"])
def update_comment(request, movie_pk, comment_pk):
    login_user = request.user
    try:
        comment = Comment.objects.get(pk=comment_pk, movies=movie_pk)
    except Comment.DoesNotExist:
        return Response(
            {"detail": "수정할 댓글이 없습니다."}, status=status.HTTP_404_NOT_FOUND
        )

    if comment.users.first() != login_user:
        return Response(
            {"detail": "다른 사람의 댓글은 수정할 수 없습니다."},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = CommentSerializer(comment, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def like_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    login_user = request.user

    if comment.users.filter(pk=login_user.pk).exists():
        return Response(
            {"detail": "자기자신의 코멘트는 좋아요 할 수 없습니다."},
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )

    if comment.liked_users.filter(pk=login_user.pk).exists():
        comment.liked_users.remove(login_user)
        return Response(
            {"status": "removed", "comment_pk": comment.pk}, status=status.HTTP_200_OK
        )
    else:
        # 좋아요 추가
        if not CommentLike.objects.filter(user=login_user, comment=comment).exists():
            # 경험치 추가
            login_user.experience += 10
            login_user.save()

        comment.liked_users.add(login_user)
        CommentLike.objects.get_or_create(user=login_user, comment=comment)
        return Response(
            {"status": "added", "comment_pk": comment.pk}, status=status.HTTP_200_OK
        )


# 로그인한 유저가 좋아요한 comment 들만
@api_view(["GET"])
def login_user_like_comment(request):
    login_user = request.user
    comments = Comment.objects.filter(liked_users=login_user)
    serializer = CommentUserLikedSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# top_5 코멘트
@api_view(["GET"])
def top_5_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    top_5_comments = movie.comments.annotate(like_count=Count("liked_users")).order_by(
        "-like_count"
    )[:5]
    serializer = CommentListSerializer(top_5_comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
