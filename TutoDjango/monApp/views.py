from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Produit, Categorie, Statut
from django.urls import reverse
from django.contrib import messages

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['param'] = self.kwargs.get('param', None)
        context['titreh1'] = "Hello DJANGO"
        context['titretitre'] = "Accueil"
        context['page_home'] = True
        return context

class AboutView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titreh1'] = "About Us"
        context['titretitre'] = "About"
        context['page_home'] = False
        context['param'] = None
        return context

class ContactView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titreh1'] = "Contact Us"
        context['titretitre'] = "Contact"
        context['page_home'] = False
        context['param'] = None
        return context

class ListProduitsView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"

class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = f"Détails du produit : {self.object.intituleProd}"
        return context

class ListCategoriesView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "categories"

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "cat"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = f"Détails de la catégorie : {self.object.nomCat}"
        context['produits'] = self.object.produits.all()
        return context

class ListStatutsView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "statuts"

class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "stt"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = f"Détails du statut : {self.object.libelle}"
        context['produits'] = self.object.produits.all()
        return context


#Partie Connexion

class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'

    def post(self, request, **kwargs):
        lgn = request.POST.get('username')
        pswrd = request.POST.get('password')
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return redirect(reverse('monApp:home'))
        else:
            return render(request, 'monApp/page_register.html')


class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', '').strip()
        mail = request.POST.get('mail', '').strip()
        password = request.POST.get('password', '').strip()

        if not (username and mail and password):
            messages.error(request, "Tous les champs sont obligatoires.")
            return render(request, self.template_name)

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d’utilisateur est déjà pris.")
            return render(request, self.template_name)

        user = User.objects.create_user(username=username, email=mail, password=password)
        user.save()
        messages.success(request, "Inscription réussie ! Vous pouvez maintenant vous connecter.")
        return redirect('monApp:login')


class DisconnectView(LogoutView):
    next_page = 'monApp:home'

