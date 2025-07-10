from django.urls import path
from . import views


app_name = 'Users'

urlpatterns = [
    path('', views.index, name='login-page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('request-access/', views.request_access, name='request-access'),
]
