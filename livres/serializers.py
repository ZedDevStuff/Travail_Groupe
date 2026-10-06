from rest_framework import serializers

from .models import Auteur, Categorie, Livre


class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = ['id', 'nom', 'prenom', 'biographie', 'created_at']
        read_only_fields = ['id', 'created_at']


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom', 'description']
        read_only_fields = ['id']


class LivreSerializer(serializers.ModelSerializer):
    auteur_detail = AuteurSerializer(source='auteur', read_only=True)
    categorie_detail = CategorieSerializer(source='categorie', read_only=True)

    class Meta:
        model = Livre
        fields = [
            'id',
            'titre',
            'isbn',
            'auteur',
            'auteur_detail',
            'categorie',
            'categorie_detail',
            'annee_publication',
            'editeur',
            'description',
            'quantite_totale',
            'quantite_disponible',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']