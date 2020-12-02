from django.urls import path
from .views import LanguagesListAPIView, AddLanguageCreateAPIView


urlpatterns = [
    path('langs/', LanguagesListAPIView.as_view(), name='lang'),
    path('add-lang/', AddLanguageCreateAPIView.as_view(), name='add_lang'),
]