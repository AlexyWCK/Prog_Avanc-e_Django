from django.urls import path
from . import views

app_name = 'monApp'

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("home/<str:param>/", views.HomeView.as_view(), name="home_with_param"),

    path("about/", views.AboutView.as_view(), name="about"),
    path('produits/', views.ListProduitsView.as_view(), name='list_produits'),
    path('produit/<int:pk>/', views.ProduitDetailView.as_view(), name='detail_produit'),
    path('categories/', views.ListCategoriesView.as_view(), name='list_categories'),
    path('categorie/<int:pk>/', views.CategorieDetailView.as_view(), name='detail_categorie'),
    path('statuts/', views.ListStatutsView.as_view(), name='list_statuts'),
    path('statut/<int:pk>/', views.StatutDetailView.as_view(), name='detail_statut'),

    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),

    path("contact/", views.ContactView, name="contact"),
    path("email-sent/", views.EmailSentView.as_view(), name="email-sent"),
]
