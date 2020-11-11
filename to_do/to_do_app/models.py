import datetime

from django.conf import settings
from django.db import models
from django.template.defaultfilters import date


class Task(models.Model):
    """
    This class is about the name and the date creation and update information of task
    """
    title = models.CharField(max_length=100, verbose_name='Name of task')
    publicated_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )


    def __str__(self):
        return self.title
