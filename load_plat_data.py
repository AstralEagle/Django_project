import os
import django

# Configurer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from menu.models import PlatDisponible
import csv
import random

def load_data_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            prix = random.uniform(9, 16)  # Prix aléatoire entre 9 et 16
            PlatDisponible.objects.create(
                nom=row['name'],
                description=row['description'],
                cuisine=row['cuisine'],
                course=row['course'],
                diet=row['diet'],
                prep_time=row['prep_time'],
                ingredients=row['ingredients'],
                instructions=row['instructions'],
                image_url=row['image_url'],
                prix=round(prix, 2)  # Prix arrondi à 2 décimales
            )
    print("Données de plats chargées avec succès.")

if __name__ == "__main__":
    load_data_from_csv('cuisine_updated.csv')
