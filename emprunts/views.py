from rest_framework import viewsets

from .models import Emprunt
from .serializers import EmpruntSerializer


class EmpruntViewSet(viewsets.ModelViewSet):
    """CRUD endpoints for book loans."""

    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer
    filterset_fields = ['utilisateur_id', 'livre_id', 'statut']
    ordering_fields = ['date_emprunt', 'date_retour_prevue']
