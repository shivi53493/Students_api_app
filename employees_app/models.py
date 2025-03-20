from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=10)
    emp_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emp_name
    