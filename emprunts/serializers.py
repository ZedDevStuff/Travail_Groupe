from rest_framework import serializers

from .models import Emprunt


class EmpruntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprunt
        fields = [
            'id',
            'utilisateur_id',
            'livre_id',
            'date_emprunt',
            'date_retour_prevue',
            'date_retour_effective',
            'statut',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'date_emprunt', 'created_at', 'updated_at']

    def validate(self, attrs):
        # A user cannot have two active loans of the same book.
        if self.instance is None:
            utilisateur_id = attrs.get('utilisateur_id')
            livre_id = attrs.get('livre_id')
            if utilisateur_id and livre_id:
                active = Emprunt.objects.filter(
                    utilisateur_id=utilisateur_id,
                    livre_id=livre_id,
                    statut=Emprunt.Statut.EN_COURS,
                ).exists()
                if active:
                    raise serializers.ValidationError(
                        "Cet utilisateur a déjà un emprunt en cours pour ce livre."
                    )
        return attrs


class ReservationSerializer(serializers.Serializer):
    """Stub serializer for book reservations."""

    utilisateur_id = serializers.IntegerField()
    livre_id = serializers.IntegerField()