from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Candidat, Recruteur, Offre
from .serializers import CandidatSerializer, RecruteurSerializer, OffreSerializer

class CandidatViewSet(viewsets.ModelViewSet):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer

class RecruteurViewSet(viewsets.ModelViewSet):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer

class OffreViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer

#Le recruteur peut consulter les informations du candidat en utilisant son nom et son prénom
class RecruteurCandidatDetailView(APIView):

    def get(self, request, nom, prenom):
        
        candidat = Candidat.objects.filter(nom=nom, prenom=prenom).first()

        if candidat:
            serializer = CandidatSerializer(candidat)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"ERREUR": "Candidat non trouvé"}, status=status.HTTP_404_NOT_FOUND)
