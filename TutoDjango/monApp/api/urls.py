from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'monApp_api'

router = DefaultRouter()
router.register(r'categories', views.CategorieViewSet, basename='categorie')
router.register(r'produits', views.ProduitViewSet, basename='produit')
router.register(r'statuts', views.StatutViewSet, basename='statut')
router.register(r'rayons', views.RayonViewSet, basename='rayon')
router.register(r'contenirs', views.ContenirViewSet, basename='contenir')

urlpatterns = [
    path('', include(router.urls)),
]