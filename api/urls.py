from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CandidatViewSet, RecruteurViewSet, OffreViewSet, RecruteurCandidatDetailView

router = DefaultRouter()
router.register(r'candidats', CandidatViewSet, basename='candidat')
router.register(r'recruteurs', RecruteurViewSet, basename='recruteur')
router.register(r'offres', OffreViewSet, basename='offre')

urlpatterns = [
    path('', include(router.urls)),
    path('recruteurs/candidats/<str:nom>/<str:prenom>/', RecruteurCandidatDetailView.as_view(), name='recruteur-candidat-detail'),
]
