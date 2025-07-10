from django.urls import path
from . import views


app_name = 'Dashboard'

urlpatterns = [
    path('student', views.student_dashboard, name='student'),
    path('teacher', views.teacher_dashboard, name='teacher'),
]
