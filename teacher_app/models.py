from django.db import models


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10)
    teacher_name = models.CharField(max_length=100)
    teacher_subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teacher_name
    