from django.urls import path
from .views import UserRegisterCreateAPIView, UserRetrieveUpdateAPIView, UserListAPIView


urlpatterns = [
    path('register/', UserRegisterCreateAPIView.as_view(), name='register'),
    path('signin/<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name='signin'),
    path('users/', UserListAPIView.as_view(), name='users'),

]
