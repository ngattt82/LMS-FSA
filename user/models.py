# models.py
from django.db import models
from django.contrib.auth.models import User as AuthUser
from role.models import Role
import os

def get_profile_image_upload_path(instance, filename):
    """
    Generate the file path for the profile image.
    """
    # Extract the file extension
    ext = filename.split('.')[-1]
    # Return the new file path
    return os.path.join('profile_images', f'{instance.username}_avt.{ext}')

class User(models.Model):
    auth_user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    profile_image = models.ImageField(upload_to=get_profile_image_upload_path, default='profile_images/default_profile.png')

    def __str__(self):
        return self.username