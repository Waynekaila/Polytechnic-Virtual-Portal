from django.db import models
from django.contrib.auth.models import User

class Annonce(models.Model):
    # Options prédéfinies pour l'objet
    OBJET_CHOICES = [
        ('Option1', 'Option 1'),
        ('Option2', 'Option 2'),
        ('Option3', 'Option 3'),
    ]

    titre = models.CharField(max_length=200)
    objet = models.CharField(max_length=50, choices=OBJET_CHOICES, default='Option1')
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)  # capture automatique de la date
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

