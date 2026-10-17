from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_no = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    semester = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username