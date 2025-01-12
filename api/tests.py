from rest_framework.test import APITestCase
from api.models import Candidat
from rest_framework import status
from django.urls import reverse
from datetime import date

class CandidatTests(APITestCase):

    def setUp(self):
       
        self.candidat_data = {
            'nom': 'EL KHADRAOUI',
            'prenom': 'Oumaima',
            'mail': 'oumaimaelkhadraoui@email.com',
            'numero_telephone': '0612345678',
            'date_naissance': '2002-02-08',  
        }

       
        self.candidat = Candidat.objects.create(**self.candidat_data)

       
        self.url = reverse('candidat-list')
        self.url_detail = reverse('candidat-detail', args=[self.candidat.id])

    def test_creer_candidat(self):
        
        response = self.client.post(self.url, self.candidat_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        
        self.assertEqual(response.data['nom'], self.candidat_data['nom'])
        self.assertEqual(response.data['prenom'], self.candidat_data['prenom'])
        self.assertEqual(response.data['mail'], self.candidat_data['mail'])
        self.assertEqual(response.data['numero_telephone'], self.candidat_data['numero_telephone'])
        self.assertEqual(response.data['date_naissance'], self.candidat_data['date_naissance'])

    def test_update_numero_telephone(self):
       
        nouveau_numero_telephone = { 
            'numero_telephone': '0611223344'
        }

        response = self.client.patch(self.url_detail, nouveau_numero_telephone, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


        self.assertEqual(response.data['numero_telephone'], nouveau_numero_telephone['numero_telephone'])


        candidat = Candidat.objects.get(id=self.candidat.id)
        self.assertEqual(candidat.numero_telephone, nouveau_numero_telephone['numero_telephone'])


        self.assertEqual(candidat.nom, self.candidat_data['nom'])
        self.assertEqual(candidat.prenom, self.candidat_data['prenom'])
        self.assertEqual(candidat.mail, self.candidat_data['mail'])

       
        self.assertEqual(candidat.date_naissance, date(2002, 2, 8))  # Comparer avec un 
