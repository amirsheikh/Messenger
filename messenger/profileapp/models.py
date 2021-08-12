from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    # Managed fields
    user     = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar   = models.ImageField(upload_to="static/avatars/", null=True, blank=True, default='static/avatars/profile.png')
    birthday = models.DateField(null=True, blank=True)
    phone    = models.CharField(max_length=32, null=True, blank=True)
    address  = models.CharField(max_length=255, null=True, blank=True)
    number   = models.CharField(max_length=32, null=True, blank=True)
    city     = models.CharField(max_length=50, null=True, blank=True)
    zip      = models.CharField(max_length=30, null=True, blank=True)
