from django.db import models
from role.models import Role
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture_url = models.URLField(max_length=255, blank=True, null=True)  # Changed to URLField for URLs

    def __str__(self):
        return self.full_name or self.username # Corrected the method name for string representation
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    learning_style = models.CharField(max_length=50, blank=True, null=True)
    preferred_language = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username

class UserPersonalization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name= 'personalize')
    recommended_courses = models.JSONField(null=True, blank=True)  # Sử dụng JSONField để lưu trữ danh sách khóa học gợi ý
    personalized_learning_path = models.TextField(blank=True, null=True)
    learning_style = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username
