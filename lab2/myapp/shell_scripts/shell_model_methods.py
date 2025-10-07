# shell_model_methods.py
import os
import django
from modellayer.models import Blog, Student, PersonProxy

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab2.settings")
django.setup()

print("=== Blog save() Override Example ===")
b, _ = Blog.objects.get_or_create(name="My First Blog", defaults={"tagline":"Hello World"})
b.save()
print("Blog Name:", b.name)
print("Slug auto-generated:", b.slug)

print("\n=== Student (Abstract Base Class) Example ===")
s, _ = Student.objects.get_or_create(name="Alice", age=20, home_group="A1")
print(f"Student: {s.name}, Age: {s.age}, Home Group: {s.home_group}")

print("\n=== Proxy Model Example ===")
pp = PersonProxy.objects.get(id=s.id)  
print(f"Proxy Full Name: {pp.full_name}")
print(pp.do_something())
