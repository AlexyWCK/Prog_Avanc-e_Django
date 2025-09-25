from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, label="Nom")
    email = forms.EmailField(label="Email")
    message = forms.CharField(max_length=1000, label="Message", widget=forms.Textarea)
