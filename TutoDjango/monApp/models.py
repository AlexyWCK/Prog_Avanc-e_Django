from django.db import models

class Categorie(models.Model):
    idCat = models.AutoField(primary_key=True)
    nomCat = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nomCat

class Statut(models.Model):
    idStatut = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle

class Produit(models.Model):
    refProd = models.AutoField(primary_key=True)
    intituleProd = models.CharField(max_length=200)
    prixUnitaireProd = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits_categorie", null=True, blank=True)
    dateFabrication = models.DateField(null=True, blank=True)
    statut = models.ForeignKey(Statut, on_delete=models.SET_NULL, null=True, blank=True, related_name="produits_statut")

    def __str__(self):
        return self.intituleProd

class Rayon(models.Model):
    idRayon = models.AutoField(primary_key=True)
    nomRayon = models.CharField(max_length=100)

    def __str__(self):
        return self.nomRayon

class Contenir(models.Model):
    id = models.AutoField(primary_key=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="contenir_produit")
    rayon = models.ForeignKey(Rayon, on_delete=models.CASCADE, related_name="contenir_rayon")
    Qte = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('produit', 'rayon')
        verbose_name = "Contenir"
        verbose_name_plural = "Contenir"

    def __str__(self):
        return f"{self.produit.intituleProd} dans {self.rayon.nomRayon} (Quantité: {self.Qte})"