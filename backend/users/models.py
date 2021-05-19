from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

AbstractUser._meta.get_field('email').blank = False
AbstractUser._meta.get_field('email').null = False
class User(AbstractUser):
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'motion',)
        unique_together = ('email',)

class FavoriteMotion(models.Model):
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    motion = models.ForeignKey('motions.Motion', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'motion',)