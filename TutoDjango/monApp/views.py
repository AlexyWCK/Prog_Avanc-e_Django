from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Produit, Categorie, Statut, Rayon, Contenir
from .forms import ProduitForm, CategorieForm, StatutForm, RayonForm, ContenirForm, ContactUsForm
from decimal import Decimal
from django.db import transaction
from django.db.models import F

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        param = self.kwargs.get('param', '')
        context['titremenu'] = "Accueil"
        context['message'] = f"Vous avez cherché : {param}" if param else "Bienvenue sur la page d'accueil"
        return context

class AboutView(TemplateView):
    template_name = "monApp/about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "À propos"
        return context

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
            messages.error(request, "Nom d’utilisateur ou mot de passe incorrect.")
            return render(request, self.template_name)

class RegisterView(CreateView):
    template_name = 'monApp/page_register.html'
    form_class = UserCreationForm
    def form_valid(self, form):
        user = form.save()
        # save optional email field if provided from the template extra input 'mail'
        mail = self.request.POST.get('mail')
        if mail:
            user.email = mail
            user.save()
        login(self.request, user)
        return redirect('monApp:home')

class DisconnectView(LogoutView):
    next_page = 'monApp:home'

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    # Template expects `prdts` and uses 'search' as the query param
    context_object_name = "prdts"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Produit.objects.filter(intituleProd__icontains=query)
        return Produit.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Liste des produits"
        return context

@method_decorator(login_required, name='dispatch')
class ProduitCreateView(CreateView):
    model = Produit
    form_class = ProduitForm
    template_name = "monApp/create_produit.html"
    def form_valid(self, form):
        prdt = form.save()
        return redirect('monApp:detail_produit', prdt.pk)

class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"
    def get_queryset(self):
        return Produit.objects.select_related('categorie', 'statut').prefetch_related('contenir_produit__rayon')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = f"Détails du produit : {self.object.intituleProd}"
        return context

@method_decorator(login_required, name='dispatch')
class ProduitUpdateView(UpdateView):
    model = Produit
    form_class = ProduitForm
    template_name = "monApp/update_produit.html"
    def form_valid(self, form):
        prdt = form.save()
        return redirect('monApp:detail_produit', prdt.pk)

@method_decorator(login_required, name='dispatch')
class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    def get_success_url(self):
        return reverse('monApp:list_produits')

from django.db.models import Count


class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    # template expects 'ctgrs'
    context_object_name = "ctgrs"
    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = Categorie.objects.annotate(nb_produits=Count('produits_categorie'))
        if query:
            return qs.filter(nomCat__icontains=query)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Liste des catégories"
        return context

@method_decorator(login_required, name='dispatch')
class CategorieCreateView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "monApp/create_categorie.html"
    def form_valid(self, form):
        cat = form.save()
        return redirect('monApp:dtl-ctgr', cat.pk)

class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    # Template expects `ctgr` as the object name
    context_object_name = "ctgr"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = f"Détails de la catégorie : {self.object.nomCat}"
        # add the products for this category
        prdts = Produit.objects.filter(categorie=self.object)
        context['prdts'] = prdts
        # provide nb_produits attribute for compatibility with template
        try:
            context['ctgr'].nb_produits = prdts.count()
        except Exception:
            pass
        return context

@method_decorator(login_required, name='dispatch')
class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "monApp/update_categorie.html"
    def form_valid(self, form):
        cat = form.save()
        return redirect('monApp:dtl-ctgr', cat.pk)

@method_decorator(login_required, name='dispatch')
class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    def get_success_url(self):
        return reverse('monApp:lst-ctgrs')

class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "statuts"
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Statut.objects.filter(libelle__icontains=query)
        return Statut.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Liste des statuts"
        return context

@method_decorator(login_required, name='dispatch')
class StatutCreateView(CreateView):
    model = Statut
    form_class = StatutForm
    template_name = "monApp/create_statut.html"
    def form_valid(self, form):
        stt = form.save()
        return redirect('monApp:dtl-stt', stt.pk)

class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "stt"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = f"Détails du statut : {self.object.libelle}"
        return context

@method_decorator(login_required, name='dispatch')
class StatutUpdateView(UpdateView):
    model = Statut
    form_class = StatutForm
    template_name = "monApp/update_statut.html"
    def form_valid(self, form):
        stt = form.save()
        return redirect('monApp:dtl-stt', stt.pk)

@method_decorator(login_required, name='dispatch')
class StatutDeleteView(DeleteView):
    model = Statut
    template_name = "monApp/delete_statut.html"
    def get_success_url(self):
        return reverse('monApp:lst-stts')

class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Rayon.objects.filter(nomRayon__icontains=query)
        return Rayon.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Liste des rayons"
        # compute total stock value per rayon to send to template as ryns_dt
        ryns = context.get('rayons', Rayon.objects.all())
        ryns_dt = []
        from django.db.models import Sum, F as _F
        for r in ryns:
            # Sum prixUnitaireProd * Qte for all Contenir in this rayon
            total = Contenir.objects.filter(rayon=r).aggregate(total_stock=Sum(_F('Qte') * _F('produit__prixUnitaireProd')))['total_stock'] or 0
            ryns_dt.append({'rayon': r, 'total_stock': total})
        context['ryns_dt'] = ryns_dt
        return context

@method_decorator(login_required, name='dispatch')
class RayonCreateView(CreateView):
    model = Rayon
    form_class = RayonForm
    template_name = "monApp/create_rayon.html"
    def form_valid(self, form):
        ryn = form.save()
        return redirect('monApp:dtl-ryn', ryn.pk)

class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "ryn"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = f"Détails du rayon : {self.object.nomRayon}"
        # Prepare product details in this rayon
        contenirs = Contenir.objects.filter(rayon=self.object).select_related('produit')
        prdts_dt = []
        total_nb = 0
        total_rayon = Decimal('0.00')
        for c in contenirs:
            prix = c.produit.prixUnitaireProd or Decimal('0.00')
            qte = c.Qte or 0
            total_prod = prix * qte
            prdts_dt.append({
                'contenir_id': c.pk,
                'produit': c.produit,
                'prix_unitaire': prix,
                'qte': qte,
                'total_produit': total_prod,
            })
            total_nb += qte
            total_rayon += total_prod
        context['prdts_dt'] = prdts_dt
        context['total_nb_produit'] = total_nb
        context['total_rayon'] = total_rayon
        return context

@method_decorator(login_required, name='dispatch')
class RayonUpdateView(UpdateView):
    model = Rayon
    form_class = RayonForm
    template_name = "monApp/update_rayon.html"
    def form_valid(self, form):
        ryn = form.save()
        return redirect('monApp:dtl-ryn', ryn.pk)

@method_decorator(login_required, name='dispatch')
class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    def get_success_url(self):
        return reverse('monApp:lst-ryns')

@method_decorator(login_required, name='dispatch')
class ContenirCreateView(CreateView):
    model = Contenir
    form_class = ContenirForm
    template_name = "monApp/create_contenir.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        try:
            rayon = Rayon.objects.get(pk=pk)
        except Rayon.DoesNotExist:
            rayon = None
        context['rayon'] = rayon
        return context

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        produit = form.cleaned_data.get('produit')
        qte = int(form.cleaned_data.get('Qte') or 0)
        try:
            rayon = Rayon.objects.get(pk=pk)
        except Rayon.DoesNotExist:
            messages.error(self.request, "Rayon introuvable.")
            return redirect('monApp:lst-ryns')

        # Use a transaction with get_or_create and F() to atomically create or update quantity
        with transaction.atomic():
            obj, created = Contenir.objects.select_for_update().get_or_create(produit=produit, rayon=rayon, defaults={'Qte': qte})
            if not created:
                # increment atomically
                Contenir.objects.filter(pk=obj.pk).update(Qte=F('Qte') + qte)
                messages.success(self.request, f"Quantité mise à jour pour {produit.intituleProd} dans {rayon.nomRayon}.")
            else:
                messages.success(self.request, f"Produit {produit.intituleProd} ajouté au rayon {rayon.nomRayon}.")
        return redirect('monApp:dtl-ryn', rayon.pk)

@method_decorator(login_required, name='dispatch')
class ContenirUpdateView(UpdateView):
    model = Contenir
    form_class = ContenirForm
    template_name = "monApp/update_contenir.html"
    def form_valid(self, form):
        cnt = form.save()
        return redirect('monApp:dtl-ryn', cnt.rayon.pk)

@method_decorator(login_required, name='dispatch')
class ContenirDeleteView(DeleteView):
    model = Contenir
    template_name = "monApp/delete_contenir.html"
    def get_success_url(self):
        return reverse('monApp:dtl-ryn', kwargs={'pk': self.object.rayon.pk})

class ContactView(FormView):
    template_name = 'monApp/contact.html'
    form_class = ContactUsForm
    def form_valid(self, form):
        form.send_email()
        return redirect('monApp:email-sent')

class EmailSentView(TemplateView):
    template_name = 'monApp/email_sent.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titremenu'] = "Message envoyé"
        return context