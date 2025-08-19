from datetime import date
from django.db.models import Q, F
from django.db import models
from makequery.models import Poll, Blog, Entry

Poll.objects.all().delete()
Blog.objects.all().delete()
Entry.objects.all().delete()

# Tạo Polls
Poll.objects.create(question="Who is the best?", pub_date=date(2005, 5, 2))
Poll.objects.create(question="What is Django?", pub_date=date(2005, 5, 6))
Poll.objects.create(question="Where are we?", pub_date=date(2006, 1, 1))

# Tạo Blog
blog = Blog.objects.create(name="My blog", tagline="Testing queries")


# Tạo Entries
Entry.objects.create(blog=blog, headline="First entry", pub_date=date(2005, 5, 2), number_of_comments=3, number_of_pingbacks=1, rating=5)
Entry.objects.create(blog=blog, headline="Second entry", pub_date=date(2007, 1, 1), number_of_comments=10, number_of_pingbacks=2, rating=8)

# --- Q OBJECTS ---

print("Q objects with OR:")
print(Poll.objects.filter(Q(question__startswith="Who") | Q(question__startswith="What")))

print("Q objects with OR + NOT:")
print(Poll.objects.filter(Q(question__startswith="Who") | ~Q(pub_date__year=2005)))

try:
    print("Q objects combined with AND:")
    print(Poll.objects.get(
        Q(question__startswith="Who"),
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
    ))
except Poll.DoesNotExist:
    print("No Poll found for combined AND query")


# --- COMPARING OBJECTS ---

some_entry = Entry.objects.all().first()
other_entry = Entry.objects.all().last()

if some_entry and other_entry:
    print("Compare entries:", some_entry == other_entry)
    print("Compare ids:", some_entry.id == other_entry.id)


# --- DELETING OBJECTS ---

e = Entry.objects.first()
if e:
    print("Deleting one entry:", e.delete())

print("Bulk delete:", Entry.objects.filter(pub_date__year=2005).delete())


