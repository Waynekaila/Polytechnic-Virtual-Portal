from django.urls import path
from . import views


app_name = 'Profiles'

urlpatterns = [
    path('', views.profile, name='profile'),
    
]
