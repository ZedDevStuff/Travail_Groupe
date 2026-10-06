from rest_framework.routers import DefaultRouter

from .views import EmpruntViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'emprunts', EmpruntViewSet, basename='emprunt')
router.register(r'reservations', ReservationViewSet, basename='reservation')

urlpatterns = router.urls