from rest_framework.test import APITestCase
from api.models import Candidat
from rest_framework import status
from django.urls import reverse

class CandidatTests(APITestCase):

    def setUp(self):
        # Données pour un candidat
        self.candidat_data = {
            'nom': 'Jean',
            'prenom': 'Dupont',
            'mail': 'jean.dupont@email.com',
            'numero_telephone': '0102030405',
            'date_naissance': '1990-01-01'
        }
        # URL de l'API pour lister et créer les candidats
        self.url = reverse('candidat-list')

    def test_creer_candidat(self):
        """Tester la création d'un candidat"""
        response = self.client.post(self.url, self.candidat_data, format='json')

        # Vérification du code de statut
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Vérification que les données renvoyées correspondent aux données envoyées
        self.assertEqual(response.data['nom'], self.candidat_data['nom'])
        self.assertEqual(response.data['prenom'], self.candidat_data['prenom'])
        self.assertEqual(response.data['mail'], self.candidat_data['mail'])
        self.assertEqual(response.data['numero_telephone'], self.candidat_data['numero_telephone'])
        self.assertEqual(response.data['date_naissance'], self.candidat_data['date_naissance'])
