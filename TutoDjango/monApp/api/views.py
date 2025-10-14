from rest_framework import viewsets, generics
from monApp.models import Categorie, Produit, Statut, Rayon, Contenir
from .serializers import CategorieSerializer, ProduitSerializer, StatutSerializer, RayonSerializer, ContenirSerializer
from datetime import datetime

# Vues génériques
class CategorieAPIView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class CategorieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class ProduitAPIView(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class ProduitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class StatutAPIView(generics.ListCreateAPIView):
    queryset = Statut.objects.all()
    serializer_class = StatutSerializer

class StatutDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statut.objects.all()
    serializer_class = StatutSerializer

class RayonAPIView(generics.ListCreateAPIView):
    queryset = Rayon.objects.all()
    serializer_class = RayonSerializer

class RayonDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rayon.objects.all()
    serializer_class = RayonSerializer

class ContenirAPIView(generics.ListCreateAPIView):
    queryset = Contenir.objects.all()
    serializer_class = ContenirSerializer

class ContenirDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contenir.objects.all()
    serializer_class = ContenirSerializer
    lookup_field = 'id'

# ModelViewSet
class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all().prefetch_related('produits_categorie')
    serializer_class = CategorieSerializer

class ProduitViewSet(viewsets.ModelViewSet):
    serializer_class = ProduitSerializer

    def get_queryset(self):
        queryset = Produit.objects.all()
        # Filtrage dynamique par date via paramètre d'URL
        datefilter = self.request.GET.get('datefilter')
        if datefilter:
            try:
                datefilter = datetime.strptime(datefilter, "%d/%m/%Y")
                queryset = queryset.filter(dateFabrication__gt=datefilter)
            except ValueError:
                pass 
        return queryset

class StatutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Statut.objects.all().prefetch_related('produits_statut')
    serializer_class = StatutSerializer

class RayonViewSet(viewsets.ModelViewSet):
    queryset = Rayon.objects.all()
    serializer_class = RayonSerializer

class ContenirViewSet(viewsets.ModelViewSet):
    queryset = Contenir.objects.all()
    serializer_class = ContenirSerializer