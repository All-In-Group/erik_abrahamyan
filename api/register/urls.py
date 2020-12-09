from django.urls import path
from .views import UserSignUpCreateAPIView, SignInView, UserListAPIView


urlpatterns = [
    path('signup/', UserSignUpCreateAPIView.as_view(), name='register'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('users/', UserListAPIView.as_view(), name='users'),

]
