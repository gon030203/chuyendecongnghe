import os
import django
from datetime import date
from modellayer.models import PersonBand, Group, Membership

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab2.settings")
django.setup()

print("=== Many-to-Many with through Example ===")
john, _ = PersonBand.objects.get_or_create(name="John Lennon")
paul, _ = PersonBand.objects.get_or_create(name="Paul McCartney")
ringo, _ = PersonBand.objects.get_or_create(name="Ringo Starr")
beatles, _ = Group.objects.get_or_create(name="The Beatles")

# Memberships
Membership.objects.get_or_create(person=john, group=beatles, date_joined=date(1960,8,1), invite_reason="Founder")
Membership.objects.get_or_create(person=paul, group=beatles, date_joined=date(1960,8,1), invite_reason="Friend")
Membership.objects.get_or_create(person=ringo, group=beatles, date_joined=date(1962,8,16), invite_reason="New drummer")

print("Members of Beatles:", list(beatles.members.all()))

# Add/create with through_defaults
beatles.members.add(
    john,
    through_defaults={"date_joined": date(1960,8,1), "invite_reason": "Co-founder again"}
)
beatles.members.create(
    name="George Harrison",
    through_defaults={"date_joined": date(1960,8,1), "invite_reason": "Lead guitarist"}
)
print("Members after add/create:", list(beatles.members.all()))
