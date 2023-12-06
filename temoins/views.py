from django.shortcuts import render
from django.http import HttpResponse
from .resources import *
# Create your views here.


def Dashboard_temoins(request):
    return render(request, 'home/dashboard/temoin_dashboard/dashboard_temoins.html')

def Create_temoin(request):
    return render(request, 'home/dashboard/temoin_dashboard/create_temoin.html')

def Edit_temoin(request):
    return render(request, 'home/dashboard/temoin_dashboard/edit_temoin.html')

def Delete_temoin(request):
    return render(request, 'home/dashboard/temoin_dashboard/delete_temoin.html')

def All_temoin(request):
    return render(request, 'home/dashboard/temoin_dashboard/all_temoin.html')

def ExportCentreVote(request):
    centre_vote_resources = CentreVoteResource()
    dataset = centre_vote_resources.export()
    response = HttpResponse(dataset.xlsx, content_type='text/xlsx')
    response['Content-Disposition'] = "attachment; filename='centre_vote.xlsx'"
    return response

def ExportPartiPolitique(request):
    parti_politique_resources = PartiPolitiqueResources()
    dataset = parti_politique_resources.export()
    response = HttpResponse(dataset.xlsx, content_type='text/xlsx')
    response['Content-Disposition'] = "attachment; filename='centre_vote.xlsx'"
    return response
    

    
