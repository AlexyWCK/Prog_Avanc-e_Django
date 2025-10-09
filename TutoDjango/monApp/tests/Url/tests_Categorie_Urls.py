from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from monApp.views import (
    CategorieListView,
    CategorieDetailView,
    CategorieCreateView,
    CategorieUpdateView,
    CategorieDeleteView,
)
from monApp.models import Categorie


class CategorieUrlsTest(TestCase):
    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTest")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_categorie_list_url_is_resolved(self):
        url = reverse('monApp:lst-ctgrs')
        self.assertEqual(resolve(url).view_name, 'monApp:lst-ctgrs')
        self.assertEqual(resolve(url).func.view_class, CategorieListView)

    def test_categorie_detail_url_is_resolved(self):
        url = reverse('monApp:dtl-ctgr', args=[self.ctgr.idCat])
        self.assertEqual(resolve(url).view_name, 'monApp:dtl-ctgr')
        self.assertEqual(resolve(url).func.view_class, CategorieDetailView)

    def test_categorie_create_url_is_resolved(self):
        url = reverse('monApp:crt-ctgr')
        self.assertEqual(resolve(url).view_name, 'monApp:crt-ctgr')
        self.assertEqual(resolve(url).func.view_class, CategorieCreateView)

    def test_categorie_update_url_is_resolved(self):
        url = reverse('monApp:ctgr-chng', args=[self.ctgr.idCat])
        self.assertEqual(resolve(url).view_name, 'monApp:ctgr-chng')
        self.assertEqual(resolve(url).func.view_class, CategorieUpdateView)

    def test_categorie_delete_url_is_resolved(self):
        url = reverse('monApp:ctgr-dlt', args=[self.ctgr.idCat])
        self.assertEqual(resolve(url).view_name, 'monApp:ctgr-dlt')
        self.assertEqual(resolve(url).func.view_class, CategorieDeleteView)

    def test_categorie_list_response_code(self):
        response = self.client.get(reverse('monApp:lst-ctgrs'))
        self.assertEqual(response.status_code, 200)

    def test_categorie_detail_response_code(self):
        url = reverse('monApp:dtl-ctgr', args=[self.ctgr.idCat])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_categorie_detail_response_code_KO(self):
        url = reverse('monApp:dtl-ctgr', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_categorie_create_response_code_OK(self):
        response = self.client.get(reverse('monApp:crt-ctgr'))
        self.assertEqual(response.status_code, 200)

    def test_categorie_update_response_code_OK(self):
        url = reverse('monApp:ctgr-chng', args=[self.ctgr.idCat])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_categorie_update_response_code_KO(self):
        url = reverse('monApp:ctgr-chng', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_categorie_delete_response_code_OK(self):
        url = reverse('monApp:ctgr-dlt', args=[self.ctgr.idCat])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_categorie_delete_response_code_KO(self):
        url = reverse('monApp:ctgr-dlt', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_redirect_after_categorie_creation(self):
        response = self.client.post(reverse('monApp:crt-ctgr'), {'nomCat': 'CategoriePourTestRedirectionCreation'})
        self.assertEqual(response.status_code, 302)
        # Redirects to detail view, check pattern
        self.assertTrue(response.url.startswith('/monApp/categorie/'))

    def test_redirect_after_categorie_updating(self):
        response = self.client.post(reverse('monApp:ctgr-chng', args=[self.ctgr.idCat]), data={"nomCat": "CategoriePourTestRedirectionMaj"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(f'/monApp/categorie/{self.ctgr.idCat}/'))

    def test_redirect_after_categorie_deletion(self):
        response = self.client.post(reverse('monApp:ctgr-dlt', args=[self.ctgr.idCat]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('monApp:lst-ctgrs'))
        self.assertFalse(Categorie.objects.filter(pk=self.ctgr.pk).exists())
