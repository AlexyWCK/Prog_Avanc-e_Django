from django import forms
from .models import Produit

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, label="Nom")
    email = forms.EmailField(label="Email")
    message = forms.CharField(max_length=1000, label="Message", widget=forms.Textarea)

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        exclude = ('categorie', 'status')