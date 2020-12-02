from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Languages
from .serializers import LanguageSerializers


class AddLanguageCreateAPIView(CreateAPIView):
    """
    This class add new language and anybody without authentication can add the language
    """
    serializer_class = LanguageSerializers

    def get_queryset(self, request):
        return Languages.object.create(lang=request.lang)


class LanguagesListAPIView(ListAPIView):
    """
    This class return list of lanugages, but it is shown only for admin
    """
    permission_classes = [IsAdminUser]
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializers