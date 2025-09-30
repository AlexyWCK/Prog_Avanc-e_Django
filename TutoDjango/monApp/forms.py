from django import forms
from .models import Produit, Categorie, Statut

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, label="Nom")
    email = forms.EmailField(label="Email")
    message = forms.CharField(max_length=1000, label="Message", widget=forms.Textarea)

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['intituleProd', 'prixUnitaireProd', 'categorie', 'statut', 'dateFabrication']
        widgets = {
            'dateFabrication': forms.DateInput(attrs={'type': 'date'}),
        }

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nomCat']
