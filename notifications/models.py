from django.db import models


class Notification(models.Model):
    """A notification sent to a user (referenced by ID across services)."""

    class Type(models.TextChoices):
        EMAIL = 'email', 'Email'
        SMS = 'sms', 'SMS'
        PUSH = 'push', 'Push'

    utilisateur_id = models.PositiveIntegerField(db_index=True)
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.EMAIL)
    sujet = models.CharField(max_length=255)
    message = models.TextField()
    lu = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Notification #{self.id} -> user {self.utilisateur_id}"
