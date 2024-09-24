from django.db import models
from category.models import Category
from subject.models import Subject
from question.models import Question, Answer
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
from module_group.models import Module  # Import the Module model instead of ModuleGroup
from django.core.files.base import ContentFile

User = get_user_model()


class Quiz(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    questions = models.ManyToManyField('question.Question')
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_quizzes')

    def __str__(self):
        return self.title

class Submission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_submissions')
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)
    submitted_file = models.FileField(upload_to='quiz_submissions/', null=True, blank=True)

    def __str__(self):
        return f"{self.student.username}'s submission for {self.quiz.title}"

    def calculate_grade(self):
        total_questions = self.quiz.questions.count()
        correct_answers = 0
        for submitted_answer in self.submitted_answers.all():
            correct_answer = submitted_answer.question.answers.filter(is_correct=True).first()
            if correct_answer and submitted_answer.text.lower().strip() == correct_answer.text.lower().strip():
                correct_answers += 1
        self.grade = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
        self.save()

class SubmittedAnswer(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='submitted_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, default='')  # Add default value here

    def __str__(self):
        return f"Answer for {self.question} in {self.submission}"
