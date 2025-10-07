from datetime import date, datetime
from models import Blog, Entry, Author  # đổi "blog" thành app bạn đã đặt (vd: makequery.models nếu bạn dùng makequery)

print("=== Retrieving all Blogs ===")
all_blogs = Blog.objects.all()
for b in all_blogs:
    print(f"- {b.id}: {b.name} | {b.tagline}")

print("\n=== Retrieving all Entries ===")
all_entries = Entry.objects.all()
for e in all_entries:
    print(f"- {e.id}: {e.headline} ({e.pub_date}) in Blog: {e.blog.name}")

print("\n=== Filtering Entries (pub_date__year=2006) ===")
entries_2006 = Entry.objects.filter(pub_date__year=2006)
for e in entries_2006:
    print(f"- {e.id}: {e.headline} ({e.pub_date})")

print("\n=== Filtering with chaining (headline startswith 'What') ===")
q1 = Entry.objects.filter(headline__startswith="What")
q2 = q1.exclude(pub_date__gte=date.today())
q3 = q1.filter(pub_date__gte=date.today())

print("QuerySet q1 (startswith 'What'):", list(q1))
print("QuerySet q2 (q1 excluding pub_date >= today):", list(q2))
print("QuerySet q3 (q1 with pub_date >= today):", list(q3))

print("\n=== Retrieving single Entry by pk=1 ===")
try:
    one_entry = Entry.objects.get(pk=1)
    print("Got Entry:", one_entry)
except Entry.DoesNotExist:
    print("No Entry found with pk=1")
except Entry.MultipleObjectsReturned:
    print("Multiple entries found with pk=1 (unexpected!)")
