from django.urls import path
from . import views


app_name = 'Calendar'

urlpatterns = [
    path('', views.calendar, name='calendar'),
    
]