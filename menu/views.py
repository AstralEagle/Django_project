from django.shortcuts import render, redirect
from .models import PlatDisponible, DessertDisponible, MenuDuJour
import random
from django.utils import timezone
from django.db import models
from .models import Commande, CommandePlat, CommandeDessert
from .forms import CommandePlatForm, CommandeDessertForm

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

    # Vérifier si un menu du jour existe déjà pour aujourd'hui
    menu_du_jour = MenuDuJour.objects.filter(date=today).first()

    if not menu_du_jour:
        plats_disponibles = list(PlatDisponible.objects.all())
        desserts_disponibles = list(DessertDisponible.objects.all())
        
        if len(plats_disponibles) < 2 or len(desserts_disponibles) < 2:
            return render(request, 'menu/menu_du_jour.html', {'deux_plats': [], 'deux_desserts': [], 'total': 0, 'frais_livraison': 0})
        
        deux_plats = random.sample(plats_disponibles, 2)
        deux_desserts = random.sample(desserts_disponibles, 2)
        
        menu_du_jour = MenuDuJour.objects.create(date=today)
        menu_du_jour.plats.set(deux_plats)
        menu_du_jour.desserts.set(deux_desserts)
        menu_du_jour.save()

    deux_plats = menu_du_jour.plats.all()
    deux_desserts = menu_du_jour.desserts.all()

    total = 0
    frais_livraison = 0

    if request.method == 'POST':
        commande = Commande.objects.create(user=request.user, adresse=request.user.adresse)

        for plat in deux_plats:
            quantite = int(request.POST.get(f'plat_{plat.id}', 0))
            if quantite > 0:
                CommandePlat.objects.create(commande=commande, plat=plat, quantite=quantite)
                total += plat.prix * quantite

        for dessert in deux_desserts:
            quantite = int(request.POST.get(f'dessert_{dessert.id}', 0))
            if quantite > 0:
                CommandeDessert.objects.create(commande=commande, dessert=dessert, quantite=quantite)
                total += dessert.prix * quantite

        if total < 20:
            frais_livraison = 3
        total += frais_livraison

        commande.total = total
        commande.frais_livraison = frais_livraison
        commande.save()

        return redirect('confirmation_commande')

    return render(request, 'menu/menu_du_jour.html', {
        'deux_plats': deux_plats,
        'deux_desserts': deux_desserts,
        'total': total,
        'frais_livraison': frais_livraison
    })

def passer_commande(request):
    plats = PlatDisponible.objects.all()
    desserts = DessertDisponible.objects.all()
    total = 0
    frais_livraison = 0

    if request.method == 'POST':
        commande = Commande.objects.create(user=request.user, adresse=request.user.adresse)
        
        for plat in plats:
            quantite = int(request.POST.get(f'plat_{plat.id}', 0))
            if quantite > 0:
                CommandePlat.objects.create(commande=commande, plat=plat, quantite=quantite)
                total += plat.prix * quantite
        
        for dessert in desserts:
            quantite = int(request.POST.get(f'dessert_{dessert.id}', 0))
            if quantite > 0:
                CommandeDessert.objects.create(commande=commande, dessert=dessert, quantite=quantite)
                total += dessert.prix * quantite
        
        if total < 20:
            frais_livraison = 3
        total += frais_livraison

        commande.total = total  # Ajoutez un champ total dans le modèle Commande si nécessaire
        commande.frais_livraison = frais_livraison  # Ajoutez un champ frais_livraison si nécessaire
        commande.save()

        return redirect('confirmation_commande')

    return render(request, 'menu/passer_commande.html', {
        'plats': plats,
        'desserts': desserts,
        'total': total,
        'frais_livraison': frais_livraison
    })

def confirmation_commande(request):
    return render(request, 'menu/confirmation_commande.html')
