from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'Profile/student_settings.html')