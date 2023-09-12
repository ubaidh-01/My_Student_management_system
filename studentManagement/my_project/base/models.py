from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()

    def __str__(self):
        return self.name