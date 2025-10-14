from rest_framework import serializers
from monApp.models import Categorie, Produit, Statut, Rayon, Contenir

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ['refProd', 'intituleProd', 'prixUnitaireProd', 'categorie', 'dateFabrication', 'statut']

class CategorieSerializer(serializers.ModelSerializer):
    produits_categorie = ProduitSerializer(many=True)
    class Meta:
        model = Categorie
        fields = ['idCat', 'nomCat', 'produits_categorie']

class StatutSerializer(serializers.ModelSerializer):
    produits_statut = ProduitSerializer(many=True)
    class Meta:
        model = Statut
        fields = ['idStatut', 'libelle', 'produits_statut']

class RayonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rayon
        fields = ['idRayon', 'nomRayon']

class ContenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenir
        fields = ['id', 'produit', 'rayon', 'Qte']