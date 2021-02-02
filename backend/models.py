from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Posts(models.Model):
    userId = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
