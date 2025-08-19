import os
import django
from datetime import date

# Setup Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab2.settings")
django.setup()

from modellayer.models import Blog, Author, Entry

print("=== Demo Creating and Updating Objects ===")

# --- Create Blog (INSERT) ---
b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
b.save()
print("Created Blog:", b)

# --- Update Blog (UPDATE) ---
b.name = "New name"
b.save()
print("Updated Blog:", b)

# --- Create another Blog ---
cheese_blog = Blog.objects.create(name="Cheddar Talk", tagline="All about cheese")
print("Created Blog:", cheese_blog)

# --- Create Entry, assign ForeignKey Blog ---
entry = Entry.objects.create(
    blog=b,
    headline="Beatles First Entry",
    body_text="Some Beatles content...",
    pub_date=date(2025, 1, 1),
)
print("Created Entry:", entry)

# --- Change ForeignKey field (Entry -> Blog) ---
entry.blog = cheese_blog
entry.save()
print(f"Updated Entry blog to: {entry.blog}")

# --- Create Authors ---
joe = Author.objects.create(name="Joe", email="joe@example.com")
john = Author.objects.create(name="John", email="john@example.com")
paul = Author.objects.create(name="Paul", email="paul@example.com")
george = Author.objects.create(name="George", email="george@example.com")
ringo = Author.objects.create(name="Ringo", email="ringo@example.com")
print("Created Authors:", joe, john, paul, george, ringo)

# --- Add single Author to Entry (ManyToMany) ---
entry.authors.add(joe)
print(f"Added Author {joe} to Entry {entry}")

# --- Add multiple Authors to Entry ---
entry.authors.add(john, paul, george, ringo)
print(f"Added multiple Authors to Entry {entry}")

