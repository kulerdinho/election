from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.


class CentreVoteAdmin(ImportExportModelAdmin):
    list_display = ('code_centre', 'nom_centre', 'ville_centre', 'district_centre',
                    'commune_centre', 'adresse_centre' )
class PartiPolitiqueAdmin(ImportExportModelAdmin):
    list_display = ('regroupement_politiuqe', 'denomination', 'sigle', 'autorite', 'arrete' )


admin.site.register(Centre_vote,CentreVoteAdmin)
admin.site.register(Regroupement_politiuqe)
admin.site.register(Parti_politique, PartiPolitiqueAdmin)
admin.site.register(Temoins)













