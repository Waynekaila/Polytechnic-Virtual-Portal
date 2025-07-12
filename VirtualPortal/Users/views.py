from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import *


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        user = request.user  # Définir l'utilisateur ici

        if user.groups.filter(name='Etudiants').exists():
            return redirect('Dashboard:student')
        else:
            return redirect('Dashboard:teacher')

    return render(request, 'Users/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            if user.groups.filter(name='Etudiants').exists():
                if not remember:
                    request.session.set_expiry(0)

                return redirect('Dashboard:student')
            else:
                return redirect('Dashboard:teacher')  
        else:
            messages.error(request, "Identifiant ou mot de passe invalide.")

    return render(request, 'Users/login.html')


def logout_view(request):
    logout(request)
    return redirect('Users:login')

def request_access(request):
	return render(request, 'Users/request_access.html')


