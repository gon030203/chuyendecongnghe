# shell_one_to_one.py
import os
import django
from modellayer.models import Place, Restaurant

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab2.settings")
django.setup()

print("=== One-to-One Example ===")
place, _ = Place.objects.get_or_create(name="Pizza Place", address="123 Main St")
restaurant, _ = Restaurant.objects.get_or_create(place=place, serves_hot_dogs=True, serves_pizza=True)

print("Restaurant:", restaurant)
print("Access Place from Restaurant:", restaurant.place)
print("Access Restaurant from Place:", place.restaurant)
