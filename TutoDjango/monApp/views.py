from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit, Categorie, Statut

def home(request, param=None):
    context = {'param': param}
    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'list_produits.html', {'prdts': prdts})

def ListCategories(request):
    ctgrs = Categorie.objects.all()
    return render(request, 'list_categories.html', {'categories': ctgrs})

def ListStatuts(request):
    stts = Statut.objects.all()
    return render(request, 'list_statuts.html', {'statuts': stts})
