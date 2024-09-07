# results/views.py
from django.shortcuts import render
from .models import Student

def result_card(request, student_id):
    student = Student.objects.get(id=student_id)
    subjects = student.subject_set.all()
    return render(request, 'results/result_card.html', {'student': student, 'subjects': subjects})
