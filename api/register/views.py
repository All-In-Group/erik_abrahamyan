from django.contrib.auth.models import User

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from appdirs import unicode

from .serializers import UserSerializer


class UserSignUpCreateAPIView(CreateAPIView):
    """
    This class create a new user
    """
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    permission_classes = [IsAdminUser, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SignInView(APIView):
    """
    This class provide signin to the system, but only authenticated user
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),
            'status': 'authenticated',
        }
        return Response(content)


