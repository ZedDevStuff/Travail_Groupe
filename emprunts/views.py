from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Emprunt
from .serializers import EmpruntSerializer, ReservationSerializer


class EmpruntViewSet(viewsets.ModelViewSet):
    """CRUD endpoints for book loans."""

    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer
    filterset_fields = ['utilisateur_id', 'livre_id', 'statut']
    ordering_fields = ['date_emprunt', 'date_retour_prevue']

    @action(detail=True, methods=['put'])
    def retour(self, request, pk=None):
        """Enregistrer le retour d'un livre emprunté."""
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    @action(detail=False, methods=['get'])
    def historique(self, request):
        """Voir l'historique complet des emprunts."""
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


class ReservationViewSet(viewsets.ViewSet):
    """Réservations pour les livres non disponibles."""

    serializer_class = ReservationSerializer

    def list(self, request):
        """Consulter la liste des réservations en attente."""
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def create(self, request):
        """Créer une réservation pour un livre non disponible."""
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
