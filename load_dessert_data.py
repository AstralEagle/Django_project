
import os
import django

# Configurer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from menu.models import DessertDisponible
import csv
import random

def load_dessert_data_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            prix = random.uniform(3, 8)  # Prix aléatoire entre 3 et 8
            DessertDisponible.objects.create(
                nom=row['recipe_name'].strip(),
                flavors=row['flavors'],
                rating=float(row['rating']),
                success=float(row['success']),
                prix=round(prix, 2)  # Prix arrondi à 2 décimales
            )
    print("Données de desserts chargées avec succès.")

if __name__ == "__main__":
    load_dessert_data_from_csv('./recipes.csv')