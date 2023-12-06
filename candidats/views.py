from django.shortcuts import render

# Create your views here.

def Dashboard(request):
    return render(request, 'home/dashboard/candidat_dashboard/dashboard_candidat.html')

def Create_candidat(request):
    return render(request, 'home/dashboard/candidat_dashboard/create_candidat.html')

def Edit_candidat(request):
    return render(request, 'home/dashboard/candidat_dashboard/edit_candidat.html')

def Delete_candidat(request):
    return render(request, 'home/dashboard/candidat_dashboard/delete_candidat.html')

def All_candidat(request):
    return render(request, 'home/dashboard/candidat_dashboard/all_candidat.html')

def Sollicite_temoins(request):
    return render(request, 'pages/candidats/compenants/sollicite_temoin.html')


