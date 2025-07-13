from django.urls import path
from . import views


app_name = 'Support'

urlpatterns = [
    path('', views.support_page, name='support'),
    
]
