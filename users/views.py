from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """CRUD endpoints for library users."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering_fields = ['username', 'date_joined']

    @action(detail=False, methods=['post'])
    def register(self, request):
        """Inscription d'un nouvel utilisateur (étudiant, enseignant, bibliothécaire)."""
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    @action(detail=False, methods=['post'])
    def login(self, request):
        """Connexion — retourne un token d'authentification."""
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    @action(detail=True, methods=['get', 'put'])
    def profile(self, request, pk=None):
        """Consulter / modifier le profil d'un utilisateur."""
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
