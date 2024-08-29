from rest_framework import serializers
from .models import PlatDisponible, DessertDisponible, Commande, CommandePlat, CommandeDessert

class PlatDisponibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatDisponible
        fields = ['id', 'nom', 'description', 'prix', 'image_url']

class DessertDisponibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DessertDisponible
        fields = ['id', 'nom', 'flavors', 'prix']

class CommandePlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandePlat
        fields = ['plat', 'quantite']

class CommandeDessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandeDessert
        fields = ['dessert', 'quantite']

class CommandeSerializer(serializers.ModelSerializer):
    plats = CommandePlatSerializer(many=True)
    desserts = CommandeDessertSerializer(many=True)

    class Meta:
        model = Commande
        fields = ['user', 'adresse', 'plats', 'desserts', 'total', 'frais_livraison', 'date_commande']

    def create(self, validated_data):
        plats_data = validated_data.pop('plats')
        desserts_data = validated_data.pop('desserts')
        commande = Commande.objects.create(**validated_data)
        
        total = 0

        for plat_data in plats_data:
            plat = plat_data['plat']
            quantite = plat_data['quantite']
            CommandePlat.objects.create(commande=commande, plat=plat, quantite=quantite)
            total += plat.prix * quantite

        for dessert_data in desserts_data:
            dessert = dessert_data['dessert']
            quantite = dessert_data['quantite']
            CommandeDessert.objects.create(commande=commande, dessert=dessert, quantite=quantite)
            total += dessert.prix * quantite

        if total < 20:
            commande.frais_livraison = 3
        commande.total = total + commande.frais_livraison
        commande.save()
        
        return commande
