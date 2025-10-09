from django.test import TestCase

from monApp.forms import CategorieForm
from monApp.models import Categorie


class CategorieFormTest(TestCase):
    def test_form_valid_data(self):
        form = CategorieForm(data={'nomCat': 'CategoriePourTest'})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data_too_long(self):
        long_name = 'CategoriePourTest' * 6  # longer than 100 chars probably
        form = CategorieForm(data={'nomCat': long_name})
        self.assertFalse(form.is_valid())
        self.assertIn('nomCat', form.errors)

    def test_form_invalid_data_missed(self):
        form = CategorieForm(data={'nomCat': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('nomCat', form.errors)

    def test_form_save(self):
        form = CategorieForm(data={'nomCat': 'CategoriePourTest'})
        self.assertTrue(form.is_valid())
        ctgr = form.save()
        self.assertEqual(ctgr.nomCat, 'CategoriePourTest')
        # idCat should be present and be an integer
        self.assertIsNotNone(ctgr.idCat)
