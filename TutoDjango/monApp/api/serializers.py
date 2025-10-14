from rest_framework import serializers
from monApp.models import Categorie, Produit, Statut, Rayon, Contenir
from datetime import datetime

class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ['refProd', 'intituleProd', 'prixUnitaireProd', 'categorie', 'dateFabrication', 'statut']

class CategorieSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['idCat', 'nomCat']

    def validate_nomCat(self, value):
        if Categorie.objects.filter(nomCat=value).exists():
            raise serializers.ValidationError('La catégorie existe déjà')
        return value

    def validate(self, data):
        if len(data['nomCat']) > 100:
            raise serializers.ValidationError('Le nom de la catégorie ne doit pas dépasser 100 caractères.')
        return data

class CategorieSerializer(serializers.ModelSerializer):
    produits_categorie = serializers.SerializerMethodField()
    
    class Meta:
        model = Categorie
        fields = ['idCat', 'nomCat', 'produits_categorie']
    
    def get_produits_categorie(self, instance):
        queryset = instance.produits_categorie.filter(dateFabrication__gte=datetime.strptime("13/08/2025", "%d/%m/%Y"))
        if queryset.count() < 2:
            return []
        serializer = ProduitSerializer(queryset, many=True)
        return serializer.data

class StatutSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Statut
        fields = ['idStatut', 'libelle']

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