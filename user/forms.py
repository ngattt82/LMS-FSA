

# from django import forms
from .models import User, Role


from django import forms
from .models import User, UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'full_name', 'role', 'profile_picture_url']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'profile_picture_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'interests', 'learning_style', 'preferred_language']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'interests': forms.Textarea(attrs={'class': 'form-control'}),
            'learning_style': forms.TextInput(attrs={'class': 'form-control'}),
            'preferred_language': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name']


from django import forms
from .models import UserPersonalization

class UserPersonalizationForm(forms.ModelForm):
    class Meta:
        model = UserPersonalization
        fields = ['recommended_courses', 'personalized_learning_path', 'learning_style']
        widgets = {
            'recommended_courses': forms.Textarea(attrs={'rows': 3}),
            'personalized_learning_path': forms.Textarea(attrs={'rows': 5}),
        }










