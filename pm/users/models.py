from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce import models as tinymce_models


class Account(AbstractUser):
    picture = models.ImageField(upload_to='media/profilepics/', blank=True)
    home = models.CharField(max_length=100, blank=True)
    interests = models.CharField(max_length=200, blank=True)
    objectives = models.CharField(max_length=200, blank=True)
    joined = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=32, blank=True)
    bio = tinymce_models.HTMLField()

    def __unicode__(self):
        return self.user.username
