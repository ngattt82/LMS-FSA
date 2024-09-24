from django.db import models
from training_program.models import TrainingProgram
from subject.models import Subject

class TrainingProgramSubjects(models.Model):
    program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.IntegerField(choices=[(i, f'Semester {i}') for i in range(1, 10)], default=1)

    class Meta:
        unique_together = ('program', 'subject', 'semester')

    def __str__(self):
        return f"{self.program} - {self.subject} - Semester {self.semester}"

