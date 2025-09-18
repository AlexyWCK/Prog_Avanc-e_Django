from django.urls import path
from . import views

app_name = 'monApp'

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("home/<str:param>/", views.HomeView.as_view(), name="home_with_param"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    path('produits/', views.ListProduitsView.as_view(), name='list_produits'),
    path('produit/<int:pk>/', views.ProduitDetailView.as_view(), name='detail_produit'),
    path('categories/', views.ListCategoriesView.as_view(), name='list_categories'),
    path('statuts/', views.ListStatutsView.as_view(), name='list_statuts'),
]
