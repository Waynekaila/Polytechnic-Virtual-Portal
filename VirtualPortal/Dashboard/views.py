from django.shortcuts import *
from django.contrib.auth.decorators import *
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from Annonces.models import *


# Create your views here.
@login_required
def dashboard(request):
    username = request.user.username
    annonces = Annonce.objects.all().order_by('-date_creation')[:3]
    
    if request.user.groups.filter(name='Etudiants').exists():
        promotion = 'Science de base'
        NbrCoursR = 14
        context = {
            'username': username,
            'promotion': promotion,
            'NbrCoursR' : NbrCoursR,
            'annonces': annonces
        }
        return render(request, 'Dashboard/student_dashboard.html', context)
    elif request.user.groups.filter(name='Enseignants').exists():
        departement = 'Science de base'
        NbrCoursE = 4
        NbrEtudiant = 120
        NbrDevoir= 5
        context = {
            'username': username,
            'departement' : departement,
            'NbrCoursE' : NbrCoursE,
            'NbrEtudiant' : NbrEtudiant,
            'NbrDevoir' : NbrDevoir,
            'annonces': annonces
        }
        return render(request, 'Dashboard/teacher_dashboard.html', context)
    else:
        return redirect('/admin/')
    
    
    
    
