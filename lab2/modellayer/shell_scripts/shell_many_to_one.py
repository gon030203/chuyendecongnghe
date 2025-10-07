import os
import django
from modellayer.models import Manufacturer, Car

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab2.settings")
django.setup()

print("=== Many-to-One Example ===")
toyota, _ = Manufacturer.objects.get_or_create(name="Toyota")
car1, _ = Car.objects.get_or_create(name="Corolla", manufacturer=toyota)
car2, _ = Car.objects.get_or_create(name="Camry", manufacturer=toyota)

print("Cars of Toyota:", list(toyota.cars.all()))
