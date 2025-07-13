from django.urls import path
from . import views


app_name = 'Assignments'

urlpatterns = [
    path('', views.assignments, name='assignments'),
    
]