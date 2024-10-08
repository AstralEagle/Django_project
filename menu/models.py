from django.db import models
from django.db import models
from django.utils import timezone
from accounts.models import Adresse
from django.conf import settings

class PlatDisponible(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    cuisine = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)
    prep_time = models.CharField(max_length=50)
    ingredients = models.TextField()
    instructions = models.TextField()
    image_url = models.URLField(max_length=500)
    prix = models.DecimalField(max_digits=5, decimal_places=2, default=10.0)  # Valeur par défaut pour le prix

    def __str__(self):
        return f"{self.nom} - {self.prix}€"


class DessertDisponible(models.Model):
    nom = models.CharField(max_length=200, default="Unnamed Dessert")
    flavors = models.TextField(default="No specific flavors")
    rating = models.FloatField(default=0.0)
    success = models.FloatField(default=0.0)
    prix = models.DecimalField(max_digits=5, decimal_places=2, default=5.0)  # Valeur par défaut pour le prix

    def __str__(self):
        return f"{self.nom} - {self.prix}€"
    
class Plat(models.Model):
    plat_disponible = models.ForeignKey(PlatDisponible, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.plat_disponible.nom

class Dessert(models.Model):
    dessert_disponible = models.ForeignKey(DessertDisponible, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.dessert_disponible.nom

class MenuDuJour(models.Model):
    date = models.DateField(default=timezone.now, unique=True)
    plats = models.ManyToManyField(PlatDisponible)
    desserts = models.ManyToManyField(DessertDisponible)

    def __str__(self):
        return f"Menu du {self.date}"
    
class Commande(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    adresse = models.ForeignKey('accounts.Adresse', on_delete=models.CASCADE)
    plats = models.ManyToManyField(PlatDisponible, through='CommandePlat')
    desserts = models.ManyToManyField(DessertDisponible, through='CommandeDessert')
    date_commande = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)  # Nouveau champ total
    frais_livraison = models.DecimalField(max_digits=4, decimal_places=2, default=0)  # Nouveau champ frais_livraison

    def __str__(self):
        return f"Commande {self.id} par {self.user.email} le {self.date_commande}"

class CommandePlat(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    plat = models.ForeignKey('menu.PlatDisponible', on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

class CommandeDessert(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    dessert = models.ForeignKey('menu.DessertDisponible', on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()