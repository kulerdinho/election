from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard-temoins/',Dashboard_temoins, name='dashboard_temoins'),
    path('create-temoin/',Create_temoin, name='create_temoin'),
    path('edit-temoin/',Edit_temoin, name='edit_temoin'),
    path('all-temoin/',All_temoin, name='all_temoin'),
    path('delete-temoin/',Delete_temoin, name='delete_temoin'),
    path(r'export-centre-vote-xlsx/$', ExportCentreVote, name="export_centre_vote"),
    path(r'export-parti-politique-xlsx/$', ExportPartiPolitique, name="export_parti_politique"),
]






