from import_export import resources
from .models import *

class CentreVoteResource(resources.ModelResource):
    class Meta:
        model = Centre_vote


class PartiPolitiqueResources(resources.ModelResource):
    class Meta:
        model = Parti_politique