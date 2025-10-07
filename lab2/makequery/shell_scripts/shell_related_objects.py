from datetime import date
from django.contrib.auth.models import User
from makequery.models import Blog, Entry, Author, EntryDetail

# Xoa du lieu cu
Blog.objects.all().delete()
Entry.objects.all().delete()
Author.objects.all().delete()
EntryDetail.objects.all().delete()
User.objects.all().delete()

# Tao Blog
blog1 = Blog.objects.create(name="My Blog", tagline="Testing relationships")

# Tao User lam Author
user1 = User.objects.create(username="john")
author1 = Author.objects.create(name="John Lennon", email="john@example.com")

# Tao Entries
e1 = Entry.objects.create(
    blog=blog1,
    headline="First entry",
    pub_date=date(2005, 5, 2),
    number_of_comments=3,
    number_of_pingbacks=1,
    rating=5,
)
e2 = Entry.objects.create(
    blog=blog1,
    headline="Second entry",
    pub_date=date(2007, 1, 1),
    number_of_comments=10,
    number_of_pingbacks=2,
    rating=8,
)

# Them relation ManyToMany voi Author
e1.authors.add(author1)
e2.authors.add(author1)

# Tao OneToOne EntryDetail
ed1 = EntryDetail.objects.create(entry=e1, details="Extra info for first entry")

print("\n=== Forward (ForeignKey) ===")
print("Entry e1 -> blog:", e1.blog)

print("\n=== Backward (Blog -> Entries) ===")
print("Blog blog1 -> entry_set:", blog1.entry_set.all())

print("\n=== ManyToMany (Entry -> Authors) ===")
print("Entry e1 -> authors:", e1.authors.all())
print("Author author1 -> entry_set:", author1.entry_set.all())

print("\n=== OneToOne (Entry -> EntryDetail) ===")
print("EntryDetail ed1 -> entry:", ed1.entry)
print("Entry e1 -> entrydetail:", e1.entrydetail)

print("\n=== Queries with related objects ===")
print("Entry.objects.filter(blog=blog1):", Entry.objects.filter(blog=blog1))
print("Entry.objects.filter(blog=blog1.id):", Entry.objects.filter(blog=blog1.id))
print("Entry.objects.filter(blog=blog1.pk):", Entry.objects.filter(blog=blog1.pk))
