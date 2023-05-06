from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    GROUPS = (
        ('librarian', 'librarian'),
        ('member', 'member'),
    )
    username = models.CharField(max_length = 255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    group = models.CharField(max_length=10, choices=GROUPS, default='member')