from django.urls import path
from . import views

app_name = 'monApp'

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home_default"),
    path("home/<str:param>/", views.home, name="home_with_param"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path('produits/', views.ListProduits, name='list_produits'),
    path('categories/', views.ListCategories, name='list_categories'),
    path('statuts/', views.ListStatuts, name='list_statuts'),
]
