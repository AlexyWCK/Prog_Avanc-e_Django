from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

app_name = 'monApp_api'

# Router API
router = DefaultRouter()
router.register(r'categories', views.CategorieViewSet, basename='categorie')
router.register(r'produits', views.ProduitViewSet, basename='produit')
router.register(r'statuts', views.StatutViewSet, basename='statut')
router.register(r'rayons', views.RayonViewSet, basename='rayon')
router.register(r'contenirs', views.ContenirViewSet, basename='contenir')

# Swagger schema
schema_view = get_schema_view(
    openapi.Info(
        title="API MonApp",
        default_version='v1',
        description="Documentation interactive de l'API Django REST",
        contact=openapi.Contact(email="ton.email@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
