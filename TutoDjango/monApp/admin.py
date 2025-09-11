from django.contrib import admin
from decimal import Decimal, ROUND_HALF_UP
from .models import Produit, Categorie, Statut, Rayon

# Inline pour créer des produits directement depuis une catégorie
class ProduitInline(admin.TabularInline):
    model = Produit
    extra = 1  # nombre de lignes vides par défaut

# Admin pour la catégorie avec les produits inline
class CategorieAdmin(admin.ModelAdmin):
    inlines = [ProduitInline]

# Filtres personnalisés pour les produits
class ProduitFilter(admin.SimpleListFilter):
    title = 'filtre produit'
    parameter_name = 'custom_status'

    def lookups(self, request, model_admin):
        return (
            ('OnLine', 'En ligne'),
            ('OffLine', 'Hors ligne'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'OnLine':
            return queryset.filter(statut_id=1)
        if self.value() == 'OffLine':
            return queryset.filter(statut_id=0)

# Actions pour mettre les produits en ligne ou hors ligne
def set_produit_online(modeladmin, request, queryset):
    queryset.update(statut_id=1)
set_produit_online.short_description = "Mettre en ligne"

def set_produit_offline(modeladmin, request, queryset):
    queryset.update(statut_id=0)
set_produit_offline.short_description = "Mettre hors ligne"

# Admin pour le modèle Produit
class ProduitAdmin(admin.ModelAdmin):
    list_display = ["refProd", "intituleProd", "prixUnitaireProd", "prixTTCProd", "dateFabrication", "categorie", "statut"]
    list_editable = ["intituleProd", "prixUnitaireProd", "dateFabrication"]
    radio_fields = {"statut": admin.VERTICAL}
    search_fields = ("intituleProd", "dateFabrication")
    list_filter = (ProduitFilter,)
    date_hierarchy = "dateFabrication"
    ordering = ("-dateFabrication",)
    actions = [set_produit_online, set_produit_offline]

    # Colonne personnalisée prix TTC
    def prixTTCProd(self, instance):
        return (instance.prixUnitaireProd * Decimal('1.20')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    prixTTCProd.short_description = "Prix TTC"
    prixTTCProd.admin_order_field = "prixUnitaireProd"

# Enregistrement des modèles dans l'admin
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Statut)
admin.site.register(Rayon)
