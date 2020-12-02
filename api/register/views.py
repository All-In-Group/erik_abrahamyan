from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import UserSerializer


class UserRegisterCreateAPIView(CreateAPIView):
    """
    This class create a new user
    """
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    permission_classes = [IsAdminUser,]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
    This class provide user change data of his profile, but changing can do admin too
    """
    authentication_classes = [BasicAuthentication, ]
    permission_classes = [IsAuthenticated | IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer




