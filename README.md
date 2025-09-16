
![logo Django](assets/django.png)
___

# TD1 - Première application Django

Projet réalisé dans le cadre du TD1 de Programmation Avancée.  
Application Django simple avec une application `monApp` contenant les pages :  
- **Home** : page d'accueil (avec et sans paramètre)  
- **Contact** : page de contact  
- **About** : page à propos

J'ai donc appris à configurer la base de la structure de Django pour mes futurs projets.

___

# TP1 - Première application Django

Dans ce TP, j’ai réalisé les exercices suivants :

Création de modèles : Produit, Categorie, Statut

Ajout de données dans la base via le shell Django

Récupération des objets avec Produit.objects.all() et affichage dans une page HTML

Affichage des catégories et statuts associés à chaque produit

Création de vues et liaison avec le fichier urls.py pour naviguer entre les pages

Ce TP m’a permis de comprendre le fonctionnement de Django, la gestion des modèles, des vues et des URL, ainsi que l’affichage dynamique des données.
___

# TD2 - Administration et redirection

Pour ce TD, j’ai travaillé sur l’administration et la navigation :

- **Interface admin Django** pour gérer `Produit`, `Categorie`, `Statut` et `Rayon`  
- **Personnalisation** : colonnes visibles (`list_display`), modification directe (`list_editable`), boutons radio (`radio_fields`), recherche (`search_fields`), filtres (`list_filter`), hiérarchie par date (`date_hierarchy`), tri (`ordering`)  
- **Relations** : ajout de produits directement dans la fiche `Categorie` via `ProduitInline`  
- **Actions personnalisées** : mettre les produits en ligne ou hors ligne  
- **Optimisation** : installation de Django Debug Toolbar pour vérifier le nombre de requêtes SQL  
- **Redirections et navigation** : redirection après certaines actions et vérification de la navigation entre les pages  

Ce TD m’a permis de découvrir l’admin Django, de personnaliser l’interface et d’optimiser l’accès aux données.
___

# TP2 - Templates et refactor

Dans ce TP, j’ai travaillé sur l’amélioration du rendu et la structure des templates :  

- **Refactor des vues** pour utiliser `render` et les templates au lieu de `HttpResponse` brut  
- **Création de `base.html`** comme template principal avec barre de navigation et footer  
- **Utilisation de blocs** (`{% block contenu %}`) pour insérer le contenu spécifique aux pages  
- **Templates spécifiques** pour chaque page : `list_produits.html`, `detail_produit.html`, `ajouter_produit.html`  
- **Liens dynamiques** avec `{% url %}` pour naviguer entre les pages  
- **Chargement des fichiers statiques** avec `{% load static %}` pour CSS et Bootstrap  
- **Navigation complète** : home, produits, catégories, statuts, about, contact

Ce TP m’a permis de structurer correctement l’affichage des pages, de rendre le code plus propre et réutilisable, et de préparer le projet pour une gestion complète des modèles et CRUD.

Séance suivante : 

- **Refactor des vues** pour utiliser `render` et les templates au lieu de `HttpResponse` brut  
- **Création de `base.html`** comme template principal avec barre de navigation et footer  
- **Utilisation de blocs** (`{% block contenu %}`) pour insérer le contenu spécifique aux pages  
- **Templates spécifiques** pour chaque page : `list_produits.html`, `detail_produit.html`, `ajouter_produit.html`  
- **Liens dynamiques** avec `{% url %}` pour naviguer entre les pages  
- **Chargement des fichiers statiques** avec `{% load static %}` pour CSS et Bootstrap  
- **Navigation complète** : home, produits, catégories, statuts, about, contact  
- **Changement de la relation Many-to-Many** avec le modèle `Contenir` pour une meilleure gestion des relations  
- **Ajout de Bootstrap** pour améliorer le style et la présentation des pages  
- **Ajout du bouton Admin** dans la barre de navigation  
- **Style amélioré** des pages : boutons, mise en page, typographie, et mise en valeur du contenu  

Ce TP m’a permis de structurer correctement l’affichage des pages, de rendre le code plus propre et réutilisable, et de préparer le projet pour une gestion complète des modèles et du CRUD.