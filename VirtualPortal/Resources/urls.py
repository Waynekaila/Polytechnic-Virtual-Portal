from django.urls import path
from . import views


app_name = 'Resources'

urlpatterns = [
    path('', views.Resources, name='resources'),
    
]