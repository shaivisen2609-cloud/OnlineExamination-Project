from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name=models.CharField(max_length=100)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.subject_name

class Exam(models.Model):
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_name=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    duration=models.PositiveIntegerField(help_text="Duration in minutes")
    total_marks=models.PositiveIntegerField()
    passing_marks=models.PositiveIntegerField()
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.exam_name

class Question(models.Model):
    exam=models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text=models.TextField()
    option_a=models.CharField(max_length=200)
    option_b=models.CharField(max_length=200)
    option_c=models.CharField(max_length=200)
    option_d=models.CharField(max_length=200)
    correct_option=models.CharField(
        max_length=1,
        choices=[
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
        ]
    )
    marks=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.question_text