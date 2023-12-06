from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Centre_vote(models.Model):
    code_centre = models.CharField(max_length=20, unique=True)
    nom_centre = models.CharField(max_length=50)
    ville_centre = models.CharField(max_length=100)
    district_centre = models.CharField(max_length=100)
    commune_centre = models.CharField(max_length=100)
    adresse_centre = models.CharField(max_length=250)



class Regroupement_politiuqe(models.Model):
    nom = models.CharField(max_length=50)
    sigle = models.CharField(max_length=50)
    autorite = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.sigle

class Parti_politique(models.Model):
    logo = models.ImageField(upload_to='parti_politique/logo/', null=True, blank=True)
    regroupement_politiuqe = models.ForeignKey(Regroupement_politiuqe, on_delete=models.CASCADE, null=True, blank=True)
    denomination = models.CharField(max_length=50)
    sigle = models.CharField(max_length=50)
    autorite = models.CharField(max_length=50)
    arrete = models.CharField(max_length=50)

    def __str__(self):
       return self.sigle
   
class Temoins(models.Model):
    # information personnallle
    photo = models.ImageField(upload_to='temoins/photos/', null=True, blank=True)
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=50)
    email = models.EmailField()
    ville = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    commune = models.CharField(max_length=50)
    adresse_physique = models.CharField(max_length=50)
    regroupement_politiuqe = models.ForeignKey(Regroupement_politiuqe, on_delete=models.CASCADE, null=True, blank=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    centre_vote = models.ForeignKey(Centre_vote, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
       return self.nom