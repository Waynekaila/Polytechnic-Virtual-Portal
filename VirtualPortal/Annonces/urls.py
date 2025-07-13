from django.urls import path
from . import views


app_name = 'Annonces'

urlpatterns = [
    path('', views.annonces, name='annonces'),
    
]
