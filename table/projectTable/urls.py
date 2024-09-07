# results/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('result/<int:student_id>/', views.result_card, name='result_card'),
]
