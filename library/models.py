from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255, default='Not Set')
    created_at = models.DateTimeField(default=datetime.now()) 

    def __str__(self):
        return self.question_text


    
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
