from django.views.generic import TemplateView, ListView
from .models import Produit, Categorie, Statut

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

class ListCategoriesView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "categories"

class ListStatutsView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "statuts"
