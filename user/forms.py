from django import forms
from .models import User, Role
from django.db import models

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'full_name', 'role', 'profile_image']
        widgets = {
            'password': forms.PasswordInput(),
            'profile_image': forms.FileInput(attrs={'multiple': False}),
        }

    def __init__(self, *args, role=None, **kwargs):
        super().__init__(*args, **kwargs)  # Initialize the parent class
        if role == 'Admin':
            self.fields['role'].queryset = Role.objects.all()
        elif role == 'Staff':
            self.fields['role'].queryset = Role.objects.filter(role_name__in=['Student', 'Lecturer'])
        else:
            self.fields['role'].queryset = Role.objects.all()

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name']



class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image']
        widgets = {
            'profile_image': forms.FileInput(attrs={'multiple': False}),
        }