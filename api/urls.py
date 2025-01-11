from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CandidatViewSet, RecruteurViewSet, OffreViewSet

router = DefaultRouter()
router.register(r'candidats', CandidatViewSet, basename='candidat')
router.register(r'recruteurs', RecruteurViewSet, basename='recruteur')
router.register(r'recruteurs', RecruteurViewSet, basename='offre')


urlpatterns = [
    path('', include(router.urls)), 
]
