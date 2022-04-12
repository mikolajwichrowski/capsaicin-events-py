from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


class Event(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    picture = models.CharField(max_length=4000)
    location = models.CharField(max_length=255)
