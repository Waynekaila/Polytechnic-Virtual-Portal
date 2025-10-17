from django.urls import path
from . import views


app_name = 'Annonces'

urlpatterns = [
    path('', views.annonces, name='annonces'),
    path('create/', views.create_annonce, name='create_annonce'),
    path('edit/<int:id>/', views.edit_annonce, name='edit_annonce'),
    path('delete/<int:id>/', views.delete_annonce, name='delete_annonce'),
]
