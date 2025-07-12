from django.urls import path
from . import views


app_name = 'Courses'

urlpatterns = [
    path('', views.courses, name='cours'),
    path('<int:cours_id>', views.courses_details, name='le_cours'),
    path('add/', views.add_course, name='add_course'),

]
