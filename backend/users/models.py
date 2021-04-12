from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    favorites = models.ManyToManyField('motions.Motion', through='FavoriteMotion')


class FavoriteMotion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    motion = models.ForeignKey('motions.Motion', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
