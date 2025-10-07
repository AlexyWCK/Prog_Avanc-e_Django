from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import Produit, Categorie, Statut, Rayon, Contenir

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, label="Nom")
    email = forms.EmailField(label="Email")
    message = forms.CharField(max_length=1000, label="Message", widget=forms.Textarea)

    def send_email(self):
        """Send an email with the contact form data.

        This is intentionally tolerant: if email settings aren't configured
        the function will fail silently so the user flow still works.
        """
        subject = f"Contact form: {self.cleaned_data.get('name') or 'Anonymous'}"
        message = self.cleaned_data.get('message', '')
        from_email = self.cleaned_data.get('email') or getattr(settings, 'DEFAULT_FROM_EMAIL', None)
        recipient = getattr(settings, 'DEFAULT_FROM_EMAIL', from_email)
        try:
            if from_email and recipient:
                send_mail(subject, message, from_email, [recipient])
        except Exception:
            # Don't raise during a simple contact form submission in dev.
            pass

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

class StatutForm(forms.ModelForm):
    class Meta:
        model = Statut
        fields = ['libelle']

class RayonForm(forms.ModelForm):
    class Meta:
        model = Rayon
        fields = ['nomRayon']

class ContenirForm(forms.ModelForm):
    class Meta:
        model = Contenir
        fields = ['produit', 'Qte']