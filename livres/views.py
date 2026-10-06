from rest_framework import viewsets

from .models import Auteur, Categorie, Livre
from .serializers import AuteurSerializer, CategorieSerializer, LivreSerializer


class AuteurViewSet(viewsets.ModelViewSet):
    """CRUD endpoints for authors."""

    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    search_fields = ['nom', 'prenom']


class CategorieViewSet(viewsets.ModelViewSet):
    """CRUD endpoints for categories."""

    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    search_fields = ['nom']


class LivreViewSet(viewsets.ModelViewSet):
    """CRUD endpoints for books."""

    queryset = Livre.objects.select_related('auteur', 'categorie').all()
    serializer_class = LivreSerializer
    search_fields = ['titre', 'isbn', 'auteur__nom']
    filterset_fields = ['categorie', 'auteur']
