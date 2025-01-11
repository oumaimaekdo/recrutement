from rest_framework import serializers
from .models import Candidat, Recruteur, Offre

class CandidatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidat
        fields = ['id', 'nom', 'prenom', 'mail', 'numero_telephone', 'date_naissance']
        

class RecruteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruteur
        fields = ['id', 'nom_entreprise', 'mail', 'numero_telephone', 'site_web']

class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = ['id', 'titre', 'description', 'date_publication', 'entreprise']