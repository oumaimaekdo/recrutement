# API de Recrutement

# Projet Backend Dev - Plateforme Recrutement

Ce projet consiste à développer une API REST pour une plateforme de recrutement en utilisant le framework Django et la base de données PostgreSQL. L'API permet aux candidats de renseigner et de consulter leurs informations personnelles, ainsi qu'aux recruteurs de consulter les informations des candidats.

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
- **PostgreSQL** : La base de données utilisée pour stocker les informations des candidats et recruteurs.
- **Visual Studio Code** (VSCode) : L'éditeur de code recommandé pour ce projet.
- **Git** : Outil de gestion de version pour suivre l'évolution du projet.
- **Django REST Framework** : Pour la création des API RESTful.
- **djangorestframework-swagger** : Pour la génération de la documentation Swagger de l'API.

## Installation

1. **Clonez le repository** :

   Dans votre terminal, clonez ce repository avec la commande suivante :

   ```bash
   git clone https://github.com/oumaimaekdo/recrutement.git
   cd recrutement

2. **Créer un environnement virtuel** :

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Linux/macOS
   venv\Scripts\activate     # Sur Windows

3. **Installer les dépendances** :   

   ```bash
   pip install django
   pip install djangorestframework
   pip install psycopg2  
   pip install djangorestframework-swagger

4. **Configuratin de la base de données** :  

Assurez-vous que PostgreSQL est installé et configuré sur votre machine. Créez une base de données et mettez à jour les paramètres de la base de données dans le fichier settings.py de Django sous DATABASES :  

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

5. **Appliquer les migrations**
