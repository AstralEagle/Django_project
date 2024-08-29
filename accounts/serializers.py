from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Adresse

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number']

class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields = ['adresse', 'ville', 'code_postal', 'pays']

class UserWithAdresseSerializer(serializers.ModelSerializer):
    adresse = AdresseSerializer()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'adresse']

    def update(self, instance, validated_data):
        adresse_data = validated_data.pop('adresse', None)
        if adresse_data:
            Adresse.objects.update_or_create(user=instance, defaults=adresse_data)
        return super().update(instance, validated_data)
