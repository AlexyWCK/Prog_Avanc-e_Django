from django.urls import path, include
from . import views

app_name = 'monApp'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/<str:param>/', views.HomeView.as_view(), name='home_with_param'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('produits/', views.ProduitListView.as_view(), name='list_produits'),
    path('produit/create/', views.ProduitCreateView.as_view(), name='crt-prdt'),
    path('produit/<int:pk>/', views.ProduitDetailView.as_view(), name='detail_produit'),
    path('produit/<int:pk>/update/', views.ProduitUpdateView.as_view(), name='prdt-chng'),
    path('produit/<int:pk>/delete/', views.ProduitDeleteView.as_view(), name='dlt-prdt'),
    path('categories/', views.CategorieListView.as_view(), name='lst-ctgrs'),
    path('categorie/<int:pk>/', views.CategorieDetailView.as_view(), name='dtl-ctgr'),
    path('categorie/create/', views.CategorieCreateView.as_view(), name='crt-ctgr'),
    path('categorie/<int:pk>/update/', views.CategorieUpdateView.as_view(), name='ctgr-chng'),
    path('categorie/<int:pk>/delete/', views.CategorieDeleteView.as_view(), name='ctgr-dlt'),
    path('statuts/', views.StatutListView.as_view(), name='lst-stts'),
    path('statut/<int:pk>/', views.StatutDetailView.as_view(), name='dtl-stt'),
    path('statut/create/', views.StatutCreateView.as_view(), name='crt-stt'),
    path('statut/<int:pk>/update/', views.StatutUpdateView.as_view(), name='stt-chng'),
    path('statut/<int:pk>/delete/', views.StatutDeleteView.as_view(), name='stt-dlt'),
    path('rayons/', views.RayonListView.as_view(), name='lst-ryns'),
    path('rayon/<int:pk>/', views.RayonDetailView.as_view(), name='dtl-ryn'),
    path('rayon/create/', views.RayonCreateView.as_view(), name='crt-ryn'),
    path('rayon/<int:pk>/update/', views.RayonUpdateView.as_view(), name='ryn-chng'),
    path('rayon/<int:pk>/delete/', views.RayonDeleteView.as_view(), name='ryn-dlt'),
    path('rayon/<int:pk>/cntnr/', views.ContenirCreateView.as_view(), name='cntnr-crt'),
    path('contenir/<int:pk>/update/', views.ContenirUpdateView.as_view(), name='cntnr-chng'),
    path('contenir/<int:pk>/delete/', views.ContenirDeleteView.as_view(), name='cntnr-dlt'),
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('email-sent/', views.EmailSentView.as_view(), name='email-sent'),
    path('api/', include('monApp.api.urls')),
]