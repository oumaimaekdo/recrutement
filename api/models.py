from django.db import models

class Candidat(models.Model): 
    nom = models.CharField(max_length=50) 
    prenom = models.CharField(max_length=50) 
    mail = models.EmailField() 
    numero_telephone = models.CharField(max_length=15) 
    date_naissance = models.DateField() 
    
    def __str__(self): 
        return f"Candidat : {self.nom} {self.prenom}" 
    

class Recruteur(models.Model): 
    nom_entreprise = models.CharField(max_length=100) 
    mail = models.EmailField() 
    numero_telephone = models.CharField(max_length=15) 
    site_web = models.CharField(max_length=100) 
    
    def __str__(self): 
        return f"Entreprise : {self.nom_entreprise}" 


class Offre(models.Model): 
    titre = models.CharField(max_length=100) 
    description = models.TextField() 
    date_publication = models.DateTimeField(auto_now_add=True) 
    entreprise = models.ForeignKey(Recruteur, on_delete=models.CASCADE)

    def __str__(self): 
        return f"Offre : {self.titre}"
