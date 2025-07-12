from django.shortcuts import *
from django.contrib.auth.decorators import *
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
#ameliorer les restrictions pour chaque groupe utilisateurs
def courses(request):
    cours_list = Course.objects.all()
    user = request.user
    if user.groups.filter(name='Professeurs').exists():
        return render(request, 'Courses/teacher_courses.html', {"cours": cours_list})
    else:
        return render(request, 'Courses/student_courses.html', {"cours": cours_list})


def courses_details(request, cours_id):
    cours = get_object_or_404(Course, pk=cours_id)
    user = request.user
    if user.groups.filter(name='Professeurs').exists():
        return render(request, 'Courses/teacher_course_detail.html', {"cours": cours})
    else:
        return render(request, 'Courses/student_course_detail.html', {"cours": cours})

def add_course(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        code = request.POST.get('code')
        credits = request.POST.get('credits')
        description = request.POST.get('description')
        if title and code and credits and description:
            Course.objects.create(
                title=title,
                code=code,
                credits=int(credits),
                description=description
            )
            return redirect('Courses:cours')  # change to your course list url name
    return render(request, 'add_course.html')