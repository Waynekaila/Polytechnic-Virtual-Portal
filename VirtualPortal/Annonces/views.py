from django.shortcuts import *
from django.contrib.auth.decorators import *
from django.db.models import *
from .models import *

@login_required
def annonces(request):
    # Toutes les annonces, les plus récentes d'abord
    annonces = Annonce.objects.all().order_by('-date_creation')

    # Filtre recherche
    query = request.GET.get('q')
    if query:
        annonces = annonces.filter(
            Q(titre__icontains=query) |
            Q(objet__icontains=query) |
            Q(description__icontains=query) |
            Q(auteur__username__icontains=query)
        )

    context = {
        'annonces': annonces,
        'query': query or '',
        'objet_choices': ['Deliberation', 'Cours', 'Examen', 'Autre'],  # tes options prédéfinies
    }
    return render(request, 'Annonces/teacher_announcements.html', context)


@login_required
def create_annonce(request):
    if request.method == 'POST':
        Annonce.objects.create(
            titre=request.POST['titre'],
            objet=request.POST['objet'],
            description=request.POST['description'],
            auteur=request.user
        )
    return redirect('Annonces:annonces')


@login_required
def edit_annonce(request, id):
    annonce = get_object_or_404(Annonce, id=id, auteur=request.user)

    if request.method == 'POST':
        annonce.titre = request.POST.get('titre')
        annonce.objet = request.POST.get('objet')
        annonce.description = request.POST.get('description')
        annonce.save()
        return redirect('Annonces:annonces')

    # On n'utilise plus de page séparée, modal JS gère tout
    return redirect('Annonces:annonces')


@login_required
def delete_annonce(request, id):
    annonce = get_object_or_404(Annonce, id=id, auteur=request.user)

    if request.method == 'POST':
        annonce.delete()
    return redirect('Annonces:annonces')

