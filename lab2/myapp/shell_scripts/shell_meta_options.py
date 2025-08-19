import os
import django
from modellayer.models import Ox

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab2.settings")
django.setup()

print("=== Ox Example with Meta Options ===")
Ox.objects.get_or_create(name="Bessie", horn_length=30)
Ox.objects.get_or_create(name="MooMoo", horn_length=25)
Ox.objects.get_or_create(name="Daisy", horn_length=40)

ox_list = Ox.objects.all()
for ox in ox_list:
    print(f"{ox.name} - {ox.horn_length} cm")
