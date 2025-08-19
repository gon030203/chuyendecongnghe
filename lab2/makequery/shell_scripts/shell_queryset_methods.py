from datetime import date
from modellayer.models import Blog, Entry


print("\n--- Limiting QuerySets ---")
print("5 entries dau tien:", Entry.objects.all()[:5])
print("Entries tu 6 den 10:", Entry.objects.all()[5:10])

print("\n--- Field lookups ---")
print("Entry co pub_date <= 2006-01-01:", Entry.objects.filter(pub_date__lte="2006-01-01"))
print("Entry headline = 'New Lennon Biography':", Entry.objects.filter(headline__exact="New Lennon Biography"))
print("Entry headline chua 'Lennon':", Entry.objects.filter(headline__contains="Lennon"))
print("Entry headline (case-insensitive) chua 'lennon':", Entry.objects.filter(headline__icontains="lennon"))

print("\n--- Spanning relationships ---")
print("Entry thuoc Blog 'Beatles Blog':", Entry.objects.filter(blog__name="Beatles Blog"))
print("Blog co entry headline chua 'Lennon':", Blog.objects.filter(entry__headline__contains="Lennon"))

print("\n--- Spanning multi-valued relationships ---")
print("Blog co entry (nam 2008 va headline chua 'Lennon'):")
print(Blog.objects.filter(entry__headline__contains="Lennon", entry__pub_date__year=2008))

print("Blog co entry headline chua 'Lennon' va entry khac nam 2008:")
print(Blog.objects.filter(entry__headline__contains="Lennon").filter(entry__pub_date__year=2008))

print("\n--- Exclude examples ---")
print("Blog exclude entry chua 'Lennon' va nam 2008:")
print(Blog.objects.exclude(entry__headline__contains="Lennon", entry__pub_date__year=2008))

print("Blog exclude entry cu the (headline chua 'Lennon' nam 2008):")
print(Blog.objects.exclude(
    entry__in=Entry.objects.filter(
        headline__contains="Lennon",
        pub_date__year=2008,
    ),
))
