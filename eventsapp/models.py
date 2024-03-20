from django.db import models

class Events(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=100)

