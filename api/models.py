from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(blank=True)

    avatar = models.CharField(max_length=255, blank=True)

    profile_image = models.CharField(max_length=255, blank=True)

    profile_links = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)