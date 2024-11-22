from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Movie, Genre, Ott, Comment
from .serializers import MovieListSerializers, WishMovieSerializer, OttListSerializers, GenreListSerializers
from .serializers import CommentSerializer, MovieCommentSerializer, CommentListSerializer

User = get_user_model()

# 영화 전체 조회
@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializers(movies, many=True, context={'request': request})
    return Response(serializer.data)


# 영화 좋아요 눌렀을 때 내 프로필 페이지에서 wish_movies 볼 수 있게 vue에서 버튼 누르면 저장시키는 로직
@api_view(['POST'])
def wish_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    if movie.wish_users.filter(id=user.id).exists():
        # 이미 좋아요를 눌렀으면 취소
        movie.wish_users.remove(user)
        return Response({'status': 'removed', 'movie_pk': movie_pk}, status=status.HTTP_200_OK)
    else:
        # 좋아요 추가
        movie.wish_users.add(user)
        return Response({'status': 'added', 'movie_pk': movie_pk}, status=status.HTTP_200_OK)

# 로그인 한 유저가 좋아요 한 영화 목록
@api_view(['GET'])
def logined_wish_movie_list(request):
    login_user = request.user
    wished_movies = Movie.objects.filter(wish_users=login_user)

    serializer = WishMovieSerializer(wished_movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def genres_list(request):
    genres = Genre.objects.all()
    serializer = GenreListSerializers(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def otts_list(request):
    otts = Ott.objects.all()
    serializer = OttListSerializers(otts, many=True)
    return Response(serializer.data)

# 코멘트 생성
@api_view(['POST', 'PUT', 'DELETE'])
def comment_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # movies, users iterable이기 때문에 단일 객체 리스트 형태로[]로 감싸줘야함
            serializer.save(movies=[movie], users=[request.user])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'PUT':
    #     serializer = 


# 유저가 작성한 comment 조회
@api_view(['GET'])
def comment_list_user(request):
    login_user = request.user
    pass
    # # 로그인한 유저랑 user_pk 다르면 is_public = True인 단어장 담아서 조회
    # if login_user != person:
    #     voca_notes = VocaNote.objects.filter(users=person)
    #     if not voca_notes.exists():
    #         return Response({'error': f'{person.username}의 단어장이 없습니다.'}, status=404)
        
    #     voca_notes = VocaNote.objects.filter(users=person, is_public=True)
    #     if person != login_user and not any(note.is_public for note in voca_notes):
    #         return Response({'error': '해당 단어장은 비공개 상태입니다.'}, status=403)
       
    # # 로그인한 유저랑 user_pk 같으며 내꺼니까
    # else:
    #     # 전체 voca_notes 리스트 조회
    #     voca_notes = VocaNote.objects.filter(users=login_user).all()
    # if voca_notes is None:
    #     return Response({'error': '단어장 데이터를 불러올 수 없습니다.'}, status=500)

    # serializer = VocaNoteSerializers(voca_notes, many=True)
    # return Response(serializer.data, status=200)

@api_view(['GET'])
def comment_list_movie(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments = Comment.objects.filter(movies=movie)
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)