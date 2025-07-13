from django.shortcuts import render

# Create your views here.

def Resources(request):
    return render(request, 'Resources/student_resources.html')  