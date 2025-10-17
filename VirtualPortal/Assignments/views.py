from django.shortcuts import *
from django.contrib.auth.decorators import *
from django.utils import *
from .models import *
from Courses.models import *


@login_required
def assignments(request):
    """
    Vue principale pour afficher les devoirs avec filtres.
    Recherche dans le titre et le nom du cours.
    """
    search_query = request.GET.get('search', '')
    cours_filter = request.GET.get('cours', '')
    statut_filter = request.GET.get('statut', '')

    devoirs = Devoir.objects.all().order_by('-date_limite')
    cours_list = Course.objects.all()

    devoirs_data = []

    for devoir in devoirs:
        # Filtrage par recherche : titre OU nom du cours
        if search_query and search_query.lower() not in devoir.titre.lower() \
            and search_query.lower() not in devoir.cours.title.lower():
            continue

        # Filtrage par cours
        if cours_filter and str(devoir.cours.id) != cours_filter:
            continue

        # Statut du devoir
        statut = devoir.statut_pour(request.user)
        if statut_filter:
            if statut_filter == "en_attente" and statut != "En attente":
                continue
            elif statut_filter == "en_cours" and statut != "En cours":
                continue
            elif statut_filter == "soumis" and statut != "En attente":
                continue
            elif statut_filter == "corrige" and statut != "Terminé":
                continue

        bouton_visible = devoir.bouton_soumettre_visible and not devoir.est_soumis_par(request.user)

        devoirs_data.append({
            'id': devoir.id,
            'titre': devoir.titre,
            'cours': devoir.cours.title,
            'date_limite': devoir.date_limite,
            'note': devoir.note,
            'statut': statut,
            'bouton_visible': bouton_visible,
        })

    if request.user.groups.filter(name='Etudiants').exists():
        return render(request, 'Assignments/student_assignments.html', {
            'devoirs': devoirs_data,
            'cours_list': cours_list,
            'request': request,
        })
    elif request.user.groups.filter(name='Enseignants').exists():
        return render(request, 'Assignments/teacher_assignments.html', {
            'devoirs': devoirs_data,
            'cours_list': cours_list,
            'request': request,
        })
    else:
        return redirect('/admin/')


@login_required
def create_devoir(request):
    if request.method == "POST":
        titre = request.POST.get("titre")
        cours_id = request.POST.get("cours")
        date_limite = request.POST.get("date_limite")
        description = request.POST.get("description", "")
        liens = request.POST.get("liens", "")
        promotion = request.POST.get("promotion", "Science de base")

        try:
            cours = Course.objects.get(id=cours_id)
        except Course.DoesNotExist:
            return redirect('Assignments:assignments')  # ou gérer l'erreur

        # Création du devoir
        Devoir.objects.create(
            titre=titre,
            cours=cours,
            date_limite=date_limite,
            description=description,
            liens=liens,
            auteur=request.user,
            promotion=promotion
        )

        return redirect('Assignments:assignments')

    # GET → afficher la page ou modal
    cours_list = Course.objects.all()
    return render(request, 'Assignments/create_devoir.html', {
        'cours_list': cours_list
    })


@login_required
def edit_devoir(request, pk):
    devoir = get_object_or_404(Devoir, pk=pk)

    if request.method == 'POST':
        titre = request.POST.get('titre')
        cours_id = request.POST.get('cours')
        date_limite = request.POST.get('date_limite')
        note = request.POST.get('note')
        description = request.POST.get('description')
        liens = request.POST.get('liens')
        promotion = request.POST.get('promotion')

        # Mise à jour
        devoir.titre = titre
        devoir.cours = get_object_or_404(Course, pk=cours_id)
        devoir.date_limite = date_limite
        devoir.note = note if note else None
        devoir.description = description
        devoir.liens = liens
        devoir.promotion = promotion
        devoir.save()

        return redirect('Assignments:assignments')

    # GET request (pré-remplir la modal)
    cours_list = Course.objects.all()
    return render(request, 'Assignments/edit_devoir.html', {
        'devoir': devoir,
        'cours_list': cours_list
    })


@login_required
def view_devoir(request, pk):
    devoir = get_object_or_404(Devoir, pk=pk)
    return render(request, 'Assignments/view_devoir.html', {'devoir': devoir})


@login_required
def correct_devoir(request, pk):
    devoir = get_object_or_404(Devoir, pk=pk)
    return render(request, 'Assignments/correct_devoir.html', {'devoir': devoir})

