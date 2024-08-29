from django.shortcuts import render
from .models import PlatDisponible, DessertDisponible, MenuDuJour
import random
from django.utils import timezone
from django.db import models

def deux_plats_du_jour(request):
    plats_disponibles = list(PlatDisponible.objects.all())
    deux_plats = random.sample(plats_disponibles, 2) if len(plats_disponibles) >= 2 else plats_disponibles
    return render(request, 'menu/deux_plats_du_jour.html', {'deux_plats': deux_plats})

def deux_desserts_du_jour(request):
    desserts_disponibles = list(DessertDisponible.objects.all())
    deux_desserts = random.sample(desserts_disponibles, 2) if len(desserts_disponibles) >= 2 else desserts_disponibles
    return render(request, 'menu/deux_desserts_du_jour.html', {'deux_desserts': deux_desserts})

def menu_du_jour(request):
    plats_disponibles = list(PlatDisponible.objects.all())
    desserts_disponibles = list(DessertDisponible.objects.all())
    
    deux_plats = random.sample(plats_disponibles, 2) if len(plats_disponibles) >= 2 else plats_disponibles
    deux_desserts = random.sample(desserts_disponibles, 2) if len(desserts_disponibles) >= 2 else desserts_disponibles
    
    return render(request, 'menu/menu_du_jour.html', {'deux_plats': deux_plats, 'deux_desserts': deux_desserts})

def menu_du_jour(request):
    today = timezone.now().date()
    yesterday = today - timezone.timedelta(days=1)

    # Vérifier si le menu du jour existe déjà
    try:
        menu_du_jour = MenuDuJour.objects.get(date=today)
    except MenuDuJour.DoesNotExist:
        # Obtenir le menu d'hier s'il existe
        try:
            yesterday_menu = MenuDuJour.objects.get(date=yesterday)
            plats_exclus = yesterday_menu.plats.all()
            desserts_exclus = yesterday_menu.desserts.all()
        except MenuDuJour.DoesNotExist:
            plats_exclus = PlatDisponible.objects.none()
            desserts_exclus = DessertDisponible.objects.none()

        # Sélectionner des plats et desserts aléatoires en excluant ceux d'hier
        plats_disponibles = PlatDisponible.objects.exclude(id__in=plats_exclus)
        desserts_disponibles = DessertDisponible.objects.exclude(id__in=desserts_exclus)

        deux_plats = random.sample(list(plats_disponibles), 2) if len(plats_disponibles) >= 2 else plats_disponibles
        deux_desserts = random.sample(list(desserts_disponibles), 2) if len(desserts_disponibles) >= 2 else desserts_disponibles

        # Créer et enregistrer le nouveau menu du jour
        menu_du_jour = MenuDuJour.objects.create(date=today)
        menu_du_jour.plats.set(deux_plats)
        menu_du_jour.desserts.set(deux_desserts)
        menu_du_jour.save()

    return render(request, 'menu/menu_du_jour.html', {'deux_plats': menu_du_jour.plats.all(), 'deux_desserts': menu_du_jour.desserts.all()})