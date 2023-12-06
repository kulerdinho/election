from django.db import models
from django.contrib.auth.models import User
from temoins.models import *

# Create your models here.
class Candidats(models.Model):
    # information personnallle
    photo = models.ImageField(upload_to='candidats/photos/', null=True, blank=True)
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField(null=True, blank=True)
    telephone = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    ville = models.CharField(max_length=100)
    district = models.CharField(max_length=100, null=True, blank=True)
    commune = models.CharField(max_length=100)
    adresse_physique =models.CharField(max_length=250)
    regroupement_politiuqe = models.ForeignKey(Regroupement_politiuqe, on_delete=models.CASCADE, null=True, blank=True)
    code_presidentiel = models.CharField(max_length=10)
    code_provincial = models.CharField(max_length=10)
    code_national = models.CharField(max_length=10)
    centre_vote = models.ManyToManyField(Centre_vote)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom

class sollicite_temoin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    temoin = models.ForeignKey(Temoins, on_delete=models.CASCADE, null=True, blank=True)
    # candidats = models.ForeignKey(Candidats, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    mission = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mission

class Reclamation(models.Model):
    temoin = models.ForeignKey(Temoins, on_delete=models.CASCADE, null=True, blank=True)
    sujet = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sujet




