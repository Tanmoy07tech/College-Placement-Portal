from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    college_id=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.college_id

