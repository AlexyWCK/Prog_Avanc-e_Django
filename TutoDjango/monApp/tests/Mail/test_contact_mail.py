from django.test import TestCase
from django.core import mail
from django.urls import reverse
from monApp.forms import ContactUsForm

class ContactMailTest(TestCase):
    def test_contact_form_sends_email(self):
        """
        Vérifie qu'un email est bien envoyé avec le formulaire de contact.
        """
        form_data = {
            'name': 'Alexy',
            'email': 'alex.wiciak@gmail.com',
            'message': 'Bonjour, ceci est un test.'
        }
        form = ContactUsForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.send_email()

        # Vérifie qu'un email a bien été envoyé
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertIn('Alexy', email.subject)
        self.assertIn('Bonjour, ceci est un test.', email.body)
        self.assertEqual(email.from_email, 'alex.wiciak@gmail.com')

    def test_contact_view_post_redirects(self):
        """
        Vérifie que la vue contact redirige vers 'email-sent' après soumission valide.
        """
        response = self.client.post(reverse('monApp:contact'), {
            'name': 'Alexy',
            'email': 'alex.wiciak@gmail.com',
            'message': 'Ceci est un test via la vue.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('monApp:email-sent'))
