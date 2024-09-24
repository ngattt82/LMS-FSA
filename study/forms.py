

from django import forms
from .models import Study

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['study_subject', 'study_link', 'image', 'description']  # Thay 'subject' bằng 'study_subject'
        widgets = {
            'study_subject': forms.Select(attrs={'class': 'form-control'}),  # Thay 'subject' bằng 'study_subject'
            'study_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Coursera link'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter description"})
        }


