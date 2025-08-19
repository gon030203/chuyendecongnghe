from django.db import models
from django.db.models import Value
from django.db.models.fields.json import KT
from makequery.models import Dog


# --- Storing and querying for None ---

Dog.objects.create(name="Max", data=None)  # SQL NULL
Dog.objects.create(name="Archie", data=Value(None, models.JSONField()))  # JSON null

print("data=None:", Dog.objects.filter(data=None))
print("data=JSON null:", Dog.objects.filter(data=Value(None, models.JSONField())))
print("data__isnull=True:", Dog.objects.filter(data__isnull=True))
print("data__isnull=False:", Dog.objects.filter(data__isnull=False))


# --- Key, index, and path transforms ---

Dog.objects.create(
    name="Rufus",
    data={
        "breed": "labrador",
        "owner": {
            "name": "Bob",
            "other_pets": [
                {
                    "name": "Fishy",
                }
            ],
        },
    },
)

Dog.objects.create(name="Meg", data={"breed": "collie", "owner": None})

print("breed=collie:", Dog.objects.filter(data__breed="collie"))
print("owner__name=Bob:", Dog.objects.filter(data__owner__name="Bob"))
print("owner__other_pets__0__name=Fishy:", Dog.objects.filter(data__owner__other_pets__0__name="Fishy"))

Dog.objects.create(name="Shep", data={"breed": "collie"})
print("owner__isnull=True:", Dog.objects.filter(data__owner__isnull=True))


# --- KT expressions ---

Dog.objects.create(
    name="Shep2",
    data={
        "owner": {"name": "Bob"},
        "breed": ["collie", "lhasa apso"],
    },
)

print(
    "KT expressions:",
    Dog.objects.annotate(
        first_breed=KT("data__breed__1"),
        owner_name=KT("data__owner__name")
    ).filter(first_breed__startswith="lhasa", owner_name="Bob")
)


# --- Containment and key lookups ---

Dog.objects.create(name="Rufus2", data={"breed": "labrador", "owner": "Bob"})
Dog.objects.create(name="Meg2", data={"breed": "collie", "owner": "Bob"})
Dog.objects.create(name="Fred", data={})

print("contains owner=Bob:", Dog.objects.filter(data__contains={"owner": "Bob"}))
print("contains breed=collie:", Dog.objects.filter(data__contains={"breed": "collie"}))

print("contained_by collie+owner:", Dog.objects.filter(data__contained_by={"breed": "collie", "owner": "Bob"}))
print("contained_by collie:", Dog.objects.filter(data__contained_by={"breed": "collie"}))

Dog.objects.create(name="Rufus3", data={"breed": "labrador"})
Dog.objects.create(name="Meg3", data={"breed": "collie", "owner": "Bob"})
print("has_key=owner:", Dog.objects.filter(data__has_key="owner"))

Dog.objects.create(name="Rufus4", data={"breed": "labrador"})
Dog.objects.create(name="Meg4", data={"breed": "collie", "owner": "Bob"})
print("has_keys=[breed, owner]:", Dog.objects.filter(data__has_keys=["breed", "owner"]))

Dog.objects.create(name="Rufus5", data={"breed": "labrador"})
Dog.objects.create(name="Meg5", data={"owner": "Bob"})
print("has_any_keys=[owner, breed]:", Dog.objects.filter(data__has_any_keys=["owner", "breed"]))
