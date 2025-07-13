from django.shortcuts import *
from django.contrib.auth.decorators import *
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib import messages
from django.core.mail import send_mail



# Create your views here.
def grades(request):
    return render(request, 'Grades/grades.html')

