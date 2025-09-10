# TD1 - Première application Django
![logo Django](assets/django.png)

## Description
Projet réalisé dans le cadre du TD1 de Programmation Avancée.  
Application Django simple avec une application `monApp` contenant les pages :  
- **Home** : page d'accueil (avec et sans paramètre)  
- **Contact** : page de contact  
- **About** : page à propos

J'ai donc appris à configurer la base de la structure de Django pour mes futurs projets.

# TP1 - Première application Django

Dans ce TP, j’ai réalisé les exercices suivants :

Création de modèles : Produit, Categorie, Statut

Ajout de données dans la base via le shell Django

Récupération des objets avec Produit.objects.all() et affichage dans une page HTML

Affichage des catégories et statuts associés à chaque produit

Création de vues et liaison avec le fichier urls.py pour naviguer entre les pages

Ce TP m’a permis de comprendre le fonctionnement de Django, la gestion des modèles, des vues et des URL, ainsi que l’affichage dynamique des données.

# TD2 - Administration et redirection

Pour le TD2, j’ai travaillé sur l’administration et l’amélioration de la navigation :  

- **Création de l’interface admin** pour gérer les modèles `Produit`, `Categorie` et `Statut` depuis Django Admin  
- **Inscription des modèles dans `admin.py`** pour pouvoir les manipuler via l’interface graphique  
- **Ajout d’une redirection vers la page d’accueil** après certaines actions (ex : connexion ou ajout d’un objet)  
- **Configuration des URL** pour que la page d’accueil soit accessible directement via `/` et non seulement via `/monApp/`  
- **Test de navigation** entre les pages Home, Contact et About, et vérification que l’admin fonctionne correctement

Ce TD m’a permis de découvrir l’interface d’administration Django, la gestion des redirections et l’amélioration de l’ergonomie de navigation de l’application.