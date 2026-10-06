from django.db import models


class Emprunt(models.Model):
    """A book loan. References users/books by ID across services."""

    class Statut(models.TextChoices):
        EN_COURS = 'en_cours', 'En cours'
        RETOURNE = 'retourne', 'Retourné'
        EN_RETARD = 'en_retard', 'En retard'

    utilisateur_id = models.PositiveIntegerField(db_index=True)
    livre_id = models.PositiveIntegerField(db_index=True)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour_prevue = models.DateField()
    date_retour_effective = models.DateField(null=True, blank=True)
    statut = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.EN_COURS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_emprunt']

    def __str__(self):
        return f"Emprunt #{self.id} (livre {self.livre_id} / user {self.utilisateur_id})"
