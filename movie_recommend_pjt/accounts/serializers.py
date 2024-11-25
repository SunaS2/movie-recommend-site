from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import ValidationError

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field, user_username

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from django.contrib.auth import get_user_model
from movies.serializers import WishMovieSerializer
import logging

logger = logging.getLogger(__name__)
User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    birth = serializers.DateField()
    study_level = serializers.CharField(max_length=10)
    nickname = serializers.CharField(
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())],  # 고유성 검사 추가
    )
    first_name = serializers.CharField(max_length=30)  # 추가
    last_name = serializers.CharField(max_length=30)  # 추가

    # def validate_nickname(self, value):
    #     """닉네임 중복 체크"""
    #     if User.objects.filter(nickname=value).exists():
    #         raise ValidationError("이 닉네임은 이미 사용 중입니다.")
    #     return value

    # def validate_email(self, value):
    #     """이메일 중복 체크"""
    #     if User.objects.filter(email=value).exists():
    #         raise ValidationError("이 이메일은 이미 사용 중입니다.")
    #     return value

    # def validate_birth(self, value):
    #     """생년월일이 범위 체크 (예: 미래 날짜나 비정상적인 날짜 처리)"""
    #     from datetime import datetime
    #     if value > datetime.today().date():
    #         raise ValidationError("생년월일은 현재 날짜 이전이어야 합니다.")
    #     return value

    def get_cleaned_data(self):
        return {
            "username": self.validated_data.get("username", ""),
            "password1": self.validated_data.get("password1", ""),
            "last_name": self.validated_data.get("last_name", ""),  # 추가
            "first_name": self.validated_data.get("first_name", ""),  # 추가
            "email": self.validated_data.get("email", ""),
            "birth": self.validated_data.get("birth", ""),
            "nickname": self.validated_data.get("nickname", ""),
            "study_level": self.validated_data.get("study_level", "A1"),
        }

    def save(self, request):
        user = super().save(request)
        user.last_name = self.validated_data.get("last_name")  # 추가
        user.first_name = self.validated_data.get("first_name")  # 추가
        user.birth = self.validated_data.get("birth")
        user.nickname = self.validated_data.get("nickname")
        user.study_level = self.validated_data.get("study_level")
        user.save()
        return user


class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=True)
    email = None

    # def validate(self, attrs):
    #     # 사용자가 입력한 username을 통해 해당 사용자 존재 여부 확인
    #     user = None
    #     try:
    #         user = get_user_model().objects.get(username=attrs.get('username'))
    #     except get_user_model().DoesNotExist:
    #         raise ValidationError("로그인된 회원 정보가 없습니다. 회원가입을 진행해주세요.")

    #     # 사용자가 존재하면 기본 로그인 로직을 호출하여 인증 진행
    #     if user and not user.check_password(attrs.get('password')):
    #         raise ValidationError("비밀번호가 일치하지 않습니다.")
        
    #     return attrs



class FollowSerializer(serializers.ModelSerializer):
    """
    followings/followers 필드를 위한 서브 직렬화
    """

    class Meta:
        model = User
        fields = ["id", "username", "nickname"]  # 필요한 필드만 포함


# 현재 로그인 한 사용자 정보 반환
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = User
        # id == pk 값
        fields = ["id", "nickname", "username"]
        read_only_fields = ["id", "username", "nickname"]  # 읽기 전용 필드



# 현재 로그인 한 사용자의 레벨 정보 
class CustomUserDetailsLevelSerializer(UserDetailsSerializer):
    class Meta:
        model = User
        fields = ["id", "nickname", "username", "experience", "achievement_level", "percent"]
        read_only_fields = ["id", "username", "nickname", "experience", "achievement_level", "percent"]




# 특정 사용자 조회
class PersonUserDetailsSerializer(UserDetailsSerializer):
    followings = FollowSerializer(many=True, read_only=True)
    followers = FollowSerializer(many=True, read_only=True)
    wish_movies = WishMovieSerializer(many=True, read_only=True)

    class Meta:
        model = User
        # id == pk 값
        fields = [
            "id",
            "username",
            "nickname",
            "study_level",
            "experience",
            "achievement_level",
            "percent",
            "followings",
            "followers",
            "wish_movies",
        ]
        read_only_fields = ["id", "followings", "followers"]  # 읽기 전용 필드


# 커스텀 회원정보변경
class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "study_level",
            "nickname",
            "first_name",
            "last_name",
            "birth",
        ]

    def validate_email(self, value):
        if User.objects.filter(email=value).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("이미 사용 중인 이메일입니다.")
        return value


# 유저 study_level만 바꾸는
class CustomUserLevelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "study_level",
        ]
