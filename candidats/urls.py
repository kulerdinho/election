from django.urls import path
from .views import *

urlpatterns = [
    path('create-candidat/',Create_candidat, name='create_candidat'),
    path('dashboard/',Dashboard, name='dashboard_page'),
    path('edit-candidat/',Edit_candidat, name='edit_candidat'),
    path('delete-candidat/',Delete_candidat, name='delete_candidat'),
    path('all-candidat/',All_candidat, name='all_candidat'),
    path('sollicite-temoins/',Sollicite_temoins, name='sollicite_temoins'),
    
]

    

