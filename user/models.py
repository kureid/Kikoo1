from django.db import models
from django.urils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.TextField()
    author = 
