from django import forms
from .models import DiscussionThread,ThreadComments
from user.models import User  # Assuming you have a User model
from subject.models import Subject
class ThreadForm(forms.ModelForm):
    created_by = forms.ModelChoiceField(queryset=User.objects.all(), required=True, empty_label="Select a user")
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), required=True, empty_label="Select a subject")

    class Meta:
        model = DiscussionThread
        fields = ['thread_title', 'thread_content', 'created_by','subject']

class CommentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True, empty_label="Select a user")
    class Meta:
        model = ThreadComments
        fields = ['user','comment_text']        