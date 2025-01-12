# Projet Backend Dev - Plateforme Recrutement

## Description du projet

Ce projet consiste à la création d'une API REST pour une plateforme de recrutement. En utilisant le framework Django et une base de données PostgreSQL, l'objectif est de développer une solution permettant aux candidats de gérer leurs informations personnelles et aux recruteurs d'accéder aux profils des candidats.

## Objectifs du projet

Fournir aux candidats un moyen de renseigner et de consulter leurs informations personnelles.
Offrir aux recruteurs un accès aux profils des candidats pour faciliter le processus de recrutement.
Mettre à disposition une documentation API interactive via Swagger pour simplifier l'intégration avec le frontend.

## Table des matières
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Exécution du projet](#exécution-du-projet)
- [Endpoints API](#endpoints-api)
- [Swagger API Documentation](#swagger-api-documentation)
- [Conception UML](#conception-uml)
- [Suivi du projet](#suivi-du-projet)

## Prérequis

Avant de pouvoir exécuter le projet, vous devez avoir installé les outils suivants sur votre machine :

- **Python 3.12.3** : Le langage utilisé pour développer l'application.
- **Django** : Le framework web utilisé pour la création de l'API.
- **PostgreSQL** : La base de données utilisée pour stocker les informations des candidats, des recruteurs et des offres.
- **Visual Studio Code** (VSCode) : L'éditeur de code recommandé pour ce projet.
- **Git** : Outil de gestion de version pour suivre l'évolution du projet.
- **Django REST Framework** : Pour la création des API RESTful.
- **djangorestframework-swagger** : Pour la génération de la documentation Swagger de l'API.

## Installation

2. **Créer un environnement virtuel** :

Afin de pouvoir gérer les dépendances, créer un environnement virtuel :

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Linux/macOS
   venv\Scripts\activate     # Sur Windows
   ```

3. **Installer les dépendances** :   

Le framework principal Django :
   ```bash
   pip install django
   ```
Création de l'API REST :
   ```bash
   pip install djangorestframework
   ```
Connecteur PostgreSQL pour Django :

   ```bash
   pip install psycopg2
   ```
Génèrer la documentation Swagger pour l'API :

   ```bash
   pip install drf-yasg
   ```

   ```bash
   pip install djangorestframework-swagger
   ```

4. **Configuration de la base de données** :

Assurez-vous que PostgreSQL est installé et configuré sur votre machine :

   ```bash
   psql --version
   ```
Créez une base de données

   ```bash
   CREATE DATABASE recrutement
   ```

Mettez à jour les paramètres de la base de données dans le fichier `settings.py` de Django sous `DATABASES` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'recrutement',
        'USER': 'postgres',
        'PASSWORD': 'oumaimaekdo',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. **Appliquer les migrations** :

Pour créer les tables dans la base de données, exécutez la commande suivante :

```bash
python manage.py makemigrations
python manage.py migrate
```

## Execution du projet

1. **Lancer le serveur de développement**

Pour lancer le serveur de développement de Django, exécutez la commande suivante :

```bash
python manage.py runserver
```

Vous pouvez accéder à l'API à l'adresse suivante dans votre navigateur : 

```text
http://127.0.0.1:8000
```

Pour accèder à la documentation Swagger : 

```text
http://127.0.0.1:8000/swagger/
```

## Modèles 

le fichier `models.py` définit les modèles pour les candidats, les recruteurs et les offres.

**Candidat**

Le candidat contient les attributs suivants : 

nom : Le nom du candidat (CharField de longueur de 50 caractères (maximum)).

prenom : Le prénom du candidat (CharField de longueur de 50 caractères (maximum)).

mail : L'email du candidat (EmailField).

numero_telephone : Le numéro de téléphone du candidat (CharField de longueur de 15 caractères (maximum)).

date_naissance : La date de naissance du candidat (de type DateField).

**Recruteur** 

Le modèle Recruteur contient les informations suivantes :

nom_entreprise : Le nom de l'entreprise du recruteur (CharField de longueur de 100 caractères (maximum)).

mail : mail du recruteur (de type EmailField).

numero_telephone : numéro de téléphone du recruteur (CharField de longueur de 15 caractères (maximum)).

site_web : Le site web de l'entreprise (URLField)

**Offre**

Le modèle Offre est définie selon les attributs suivants : 

titre : titre de l'offre (CharField de longueur de 100 caractères (maximum))
Description : description de l'offre (TextField)
date_publication : date à laquelle a été publié l'offre (DateTimeField)
entreprise : l'entreprise qui a publié l'offre (CharField de longueur de 100 caractères (maximum))

**Serializers**

Le fichier serializers.py définit comment les modèles de données sont convertis en format JSON (et inversement). Chaque modèle a son propre sérializer.

**Vues**
Le fichier views.py définit les vues pour les endpoints de l'API. Chaque vue correspond à un modèle et permet de gérer les différentes requêtes HTTP.

Vue candidat La vue CandidatViewSet expose les opérations create, retrieve, update, et destroy pour les candidats.

Vue recruteur De manière similaire, la vue RecruteurViewSet permet de gérer les opérations CRUD pour les recruteurs.

**URLs**

Le fichier urls.py définit les routes pour l'API. Chaque vue est enregistrée dans un routeur qui expose les endpoints pour les candidats et les recruteurs.

## Auteur

Oumaima EL KHADRAOUI



