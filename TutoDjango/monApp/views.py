from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit, Categorie, Statut

def home(request, param=None):
    if param:
        return HttpResponse(f"<h1>Home</h1><p>Bonjour {param} !</p>")
    else:
        return HttpResponse("<h1>Home</h1><p>Bienvenue sur la page d'accueil</p>")

def contact(request):
    return HttpResponse("<h1>Contact Us</h1><p>Voici notre page de contact.</p>")

def about(request):
    return HttpResponse("<h1>About Us</h1><p>Voici la page à propos de nous.</p>")

def ListProduits(request):
    prdts = Produit.objects.all()
    liste = "".join(f"<li>{p.intituleProd}</li>" for p in prdts)
    html = f"""
    <html>
    <body>
        <h1>Liste des produits</h1>
        <ul>
            {liste}
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html)

def ListCategories(request):
    ctgrs = Categorie.objects.all()
    html = "<h2>Liste des catégories</h2><ul>"
    for c in ctgrs:
        html += f"<li>{c.nomCat}</li>"
    html += "</ul>"
    return HttpResponse(html)

def ListStatuts(request):
    stts = Statut.objects.all()
    html = "<ul>"
    for s in stts:
        html += f"<li>{s.libelle}</li>"
    html += "</ul>"
    return HttpResponse(html)
