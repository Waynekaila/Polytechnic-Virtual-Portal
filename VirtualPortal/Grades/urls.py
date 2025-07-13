from django.urls import path
from . import views


app_name = 'Grades'

urlpatterns = [
    path('', views.grades, name='grade'),
    
]
