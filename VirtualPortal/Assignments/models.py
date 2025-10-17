from django.db import *
from django.contrib.auth.models import *
from Courses.models import *
from django.utils import *


class Devoir(models.Model):
    PROMOTIONS = [
        ('Science de base', 'Science de base'),
        ('Informatique', 'Informatique'),
        ('Mathématiques', 'Mathématiques'),
        ('Physique', 'Physique'),
        ('Chimie', 'Chimie'),
    ]

    titre = models.CharField(max_length=200)
    cours = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='devoirs')
    date_limite = models.DateTimeField()
    note = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    liens = models.TextField(blank=True, help_text="Séparer plusieurs liens par des virgules")
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    afficher_soumettre = models.BooleanField(default=True)
    promotion = models.CharField(max_length=50, choices=PROMOTIONS, default='Science de base')

    class Meta:
        ordering = ['-date_limite']

    def __str__(self):
        return f"{self.titre} - {self.cours.nom}"

    def est_soumis_par(self, user):
        return self.soumissions.filter(etudiant=user).exists()

    @property
    def bouton_soumettre_visible(self):
        now = timezone.now()
        return self.afficher_soumettre and now <= self.date_limite

    def statut_pour(self, user):
        now = timezone.now()
        if now <= self.date_limite:
            return "En attente" if self.est_soumis_par(user) else "En cours"
        else:
            return "Terminé"

class DevoirSoumis(models.Model):
    devoir = models.ForeignKey(Devoir, on_delete=models.CASCADE, related_name='soumissions')
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devoirs_soumis')
    fichier = models.FileField(upload_to='devoirs_soumis/')
    date_soumission = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('devoir', 'etudiant')

    def __str__(self):
        return f"{self.devoir.titre} soumis par {self.etudiant.username}"

