from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
import os

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nom du cours")
    code = models.CharField(max_length=15, verbose_name="Code du cour")
    credits = models.IntegerField(verbose_name="Nombre de credits")
    description = models.TextField(verbose_name="Description")
    #image_mise_en_avant = models.ImageField(verbose_name="Image mise en avant")

    #prerequis=
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Cour"
        verbose_name_plural = "Cours"
