from django.urls import path

from .views import TaskListAPIView, TaskCreateAPI, TaskRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('list-task/', TaskListAPIView.as_view(), name='list_tasks'),
    path('create-task/', TaskCreateAPI.as_view(), name='create_task'),
    path('change-task/<int:pk>', TaskRetrieveUpdateDestroyAPIView.as_view(), name='RUD_task'),
]