from django.shortcuts import render
from django.http import HttpResponse

def home(request, param=None):
    if param:
        return HttpResponse(f"<h1>Home</h1><p>Bonjour {param} !</p>")
    else:
        return HttpResponse("<h1>Home</h1><p>Bienvenue sur la page d'accueil</p>")

def contact(request):
    return HttpResponse("<h1>Contact Us</h1><p>Voici notre page de contact.</p>")

def about(request):
    return HttpResponse("<h1>About Us</h1><p>Voici la page à propos de nous.</p>")
