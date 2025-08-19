import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab2.settings")
django.setup()

from modellayer.models import Person, Runner, Item

print("=== Basic Models Example ===")

# --- Person Example ---
p, created = Person.objects.get_or_create(first_name="An", last_name="Nguyen")
print("Created Person:", p)
print("Full Name (property):", p.full_name)


if hasattr(p, "birth_date"):
    print("Baby Boomer Status (method):", p.baby_boomer_status())

# --- Runner Example (Choices) ---
r, created = Runner.objects.get_or_create(name="Lan", medal=Runner.MedalType.GOLD)
print("Runner:", r)
print("Medal Display:", r.get_medal_display())

# --- Item with UUID ---
i, created = Item.objects.get_or_create(name="Laptop")
print("UUID Item:", i.id, "-", i.name)
