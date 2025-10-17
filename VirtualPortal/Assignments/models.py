from django.db import *
from django.contrib.auth.models import *
from Courses.models import * # Assure-toi d'avoir un modèle Cours

class Devoir(models.Model):
    titre = models.CharField(max_length=200)
    cours = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='devoirs')
    date_limite = models.DateTimeField()
    note = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_limite']

    def __str__(self):
        return f"{self.titre} - {self.cours.nom}"


class DevoirLien(models.Model):
    devoir = models.ForeignKey(Devoir, on_delete=models.CASCADE, related_name='liens')
    lien = models.URLField(blank=True)
    fichier = models.FileField(upload_to='devoirs/', blank=True, null=True)

    def __str__(self):
        return self.lien or str(self.fichier)

