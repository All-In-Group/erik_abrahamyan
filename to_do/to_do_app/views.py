from django.shortcuts import render
from rest_framework import generics

from .models import Task
from .serializer import TaskSerializer


class TaskListAPIView(generics.ListAPIView):
    """
    The class show all list of tasks
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateAPI(generics.CreateAPIView):
    """
    This class return all tasks which created
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class provides list, update and delete functionality
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
