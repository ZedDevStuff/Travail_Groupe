from rest_framework.routers import DefaultRouter

from .views import AuteurViewSet, CategorieViewSet, LivreViewSet

router = DefaultRouter()
router.register(r'auteurs', AuteurViewSet, basename='auteur')
router.register(r'categories', CategorieViewSet, basename='categorie')
router.register(r'livres', LivreViewSet, basename='livre')

urlpatterns = router.urls