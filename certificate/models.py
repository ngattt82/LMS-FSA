from django.db import models
from user.models import User
from subject.models import Subject
# Create your models here.
class Certificate(models.Model):
    certificate_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    issue_date = models.DateField()
    certificate_url = models.CharField(max_length=255)
    


    def __str__(self):
        return self.certificate_url