from django.views.generic import TemplateView, ListView
from .models import Produit, Categorie, Statut

class HomeView(TemplateView):
    template_name = "monApp/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['param'] = self.kwargs.get('param', None)
        return context

class ContactView(TemplateView):
    template_name = "monApp/contact.html"

class AboutView(TemplateView):
    template_name = "monApp/about.html"

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
