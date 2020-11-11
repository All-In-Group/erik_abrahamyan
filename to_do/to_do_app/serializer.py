import datetime

from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer class
    """
    class Meta:
        model = Task
        fields = ['id', 'title', 'publicated_at', 'updated_at']


