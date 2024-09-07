# results/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    marks = models.IntegerField()
    max_marks = models.IntegerField()

    def __str__(self):
        return self.name

    def percentage(self):
        return (self.marks / self.max_marks) * 100

    def grade(self):
        percentage = self.percentage()
        if percentage >= 90:
            return 'A'
        elif percentage >= 75:
            return 'B'
        elif percentage >= 50:
            return 'C'
        else:
            return 'D'
