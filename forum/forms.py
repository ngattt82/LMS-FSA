from django import forms
from .models import ForumQuestion, ForumComment, Reply

class ForumQuestionForm(forms.ModelForm):
    class Meta:
        model = ForumQuestion
        fields = ['subject', 'title', 'content']

class ForumCommentForm(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ['content']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
