from rest_framework import serializers
from monApp.models import Categorie, Produit, Statut, Rayon, Contenir

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['idCat', 'nomCat']

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ['refProd', 'intituleProd', 'prixUnitaireProd', 'categorie', 'dateFabrication', 'statut']

class StatutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statut
        fields = ['idStatut', 'libelle']

class RayonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rayon
        fields = ['idRayon', 'nomRayon']

class ContenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenir
        fields = ['id', 'produit', 'rayon', 'Qte']