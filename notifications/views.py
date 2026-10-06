from rest_framework import viewsets

from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    """CRUD endpoints for user notifications."""

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filterset_fields = ['utilisateur_id', 'type', 'lu']
    ordering_fields = ['created_at']
