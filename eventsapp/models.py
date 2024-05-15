from django.db import models
from django.contrib.auth.models import User

class Events(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    registered_users = models.ManyToManyField(User, related_name='registered_events')

