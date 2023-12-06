from django.shortcuts import render
from candidats.models import *
from temoins.models import *

def base(request):
    return render(request, 'base.html')

def home(request):
    all_centre_vote = Centre_vote.objects.all().order_by('id')
    all_regroupe_polit = Regroupement_politiuqe.objects.all()
    all_temoin = Temoins.objects.all().order_by('-id')
    all_candit = Candidats.objects.all().order_by('-id')

    mrj = {
        "all_centre_vote": all_centre_vote,
        "all_regroupe_polit": all_regroupe_polit,
        "all_temoin": all_temoin,
        'all_candit': all_candit,
    }
    return render(request, 'home/home.html', mrj)





