from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import (
    UserRegisterSerializer,
    UserResetPasswordSerializer,
    UserSerializer,
)


# TODO: APIVIEW
class UserRegisterView(generics.CreateAPIView):
    """
    POST - 유저를 생성합니다.
    """

    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer


class UserAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self, queryset=None):
        return self.request.user

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: UserSerializer,
            status.HTTP_401_UNAUTHORIZED: "인증 필요",
        }
    )
    def get(self, request, *args, **kwargs):
        """
        유저 정보 조회

        유저 정보를 반환 합니다.
        """
        self.user = self.get_object()
        serializer = self.serializer_class(self.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: "유저 정보 수정 요청이 정상적으로 처리됨",
            status.HTTP_400_BAD_REQUEST: "잘못된 요청",
            status.HTTP_401_UNAUTHORIZED: "인증 필요",
        },
    )
    def put(self, request, *args, **kwargs):

        """
        유저 정보 수정

        유저 정보를 수정 합니다.
        """
        self.user = self.get_object()

        serializer = self.serializer_class(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.user.username = serializer.validated_data.get(
            "username", self.user.username
        )
        # 이메일 수정 X
        # self.user.email = serializer.validated_data.get("email", self.user.email)
        self.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserResetPasswordAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserResetPasswordSerializer

    def get_object(self, queryset=None):
        return self.request.user

    @swagger_auto_schema(
        request_body=UserResetPasswordSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: "비밀번호 수정 요청이 정상적으로 처리됨",
            status.HTTP_400_BAD_REQUEST: "잘못된 요청",
            status.HTTP_401_UNAUTHORIZED: "인증 필요",
        },
    )
    def put(self, request, *args, **kwargs):
        """
        유저 패스워드 변경

        유저 패스워드를 변경 합니다.
        """
        self.user = self.get_object()

        serializer = self.serializer_class(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)

        old_password = serializer.data.get("old_password")
        if not self.user.check_password(old_password):
            return Response(
                {"old_password": ["잘못된 패스워드 입니다."]}, status=status.HTTP_400_BAD_REQUEST
            )

        self.user.set_password(serializer.data.get("password"))
        self.user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
