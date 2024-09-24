from django import forms
from .models import CollaborationGroup
from subject.models import Subject
from user.models import User
class CollaborationGroupForm(forms.ModelForm):
    class Meta:
        model = CollaborationGroup
        fields = ['group_name', 'created_by', 'course']
        widgets = {
            'created_by': forms.Select(),  # Assuming created_by is set programmatically
            'course': forms.Select(),  # Drop-down list for selecting subjects
        }