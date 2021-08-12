from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    # Managed fields
    user     = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar   = models.ImageField(upload_to="static/avatars/", null=True, blank=True, default='static/avatars/profile.png')
