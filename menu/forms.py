from django import forms
from .models import CommandePlat, CommandeDessert

class CommandePlatForm(forms.ModelForm):
    quantite = forms.IntegerField(min_value=1, initial=1, label='Quantité')

    class Meta:
        model = CommandePlat
        fields = ['quantite']

class CommandeDessertForm(forms.ModelForm):
    quantite = forms.IntegerField(min_value=1, initial=1, label='Quantité')

    class Meta:
        model = CommandeDessert
        fields = ['quantite']
