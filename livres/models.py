from django.db import models


class Auteur(models.Model):
    """Author of one or more books."""

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True)
    biographie = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nom', 'prenom']

    def __str__(self):
        return f"{self.prenom} {self.nom}".strip()


class Categorie(models.Model):
    """Book category/genre."""

    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Livre(models.Model):
    """A book in the library catalog."""

    titre = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True, blank=True)
    auteur = models.ForeignKey(Auteur, on_delete=models.PROTECT, related_name='livres')
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, related_name='livres')
    annee_publication = models.PositiveIntegerField(null=True, blank=True)
    editeur = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    quantite_totale = models.PositiveIntegerField(default=1)
    quantite_disponible = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['titre']

    def __str__(self):
        return self.titre
