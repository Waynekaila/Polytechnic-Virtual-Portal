from django.urls import path
from . import views

app_name = 'Assignments'

urlpatterns = [
    path('', views.assignments, name='assignments'),
    path('create/', views.create_devoir, name='create'),
    path('<int:pk>/edit/', views.edit_devoir, name='edit'),  # <- correcte
    path('<int:pk>/view/', views.view_devoir, name='view'),
    path('<int:pk>/correct/', views.correct_devoir, name='correct'),
]

