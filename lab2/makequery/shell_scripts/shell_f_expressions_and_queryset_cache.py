from datetime import timedelta
from django.db.models import F, Min, OuterRef, Subquery, Sum
from makequery.models import Blog, Entry


# F() comparisons
print(Entry.objects.filter(number_of_comments__gt=F("number_of_pingbacks")))
print(Entry.objects.filter(number_of_comments__gt=F("number_of_pingbacks") * 2))
print(Entry.objects.filter(rating__lt=F("number_of_comments") + F("number_of_pingbacks")))
print(Entry.objects.filter(authors__name=F("blog__name")))
print(Entry.objects.filter(mod_date__gt=F("pub_date") + timedelta(days=3)))
print(F("somefield").bitand(16))

# Transforms
print(Entry.objects.filter(pub_date__year=F("mod_date__year")))
print(Entry.objects.aggregate(first_published_year=Min("pub_date__year")))

print(
    Entry.objects.values("pub_date__year").annotate(
        top_rating=Subquery(
            Entry.objects.filter(pub_date__year=OuterRef("pub_date__year"))
            .order_by("-rating")
            .values("rating")[:1]
        ),
        total_comments=Sum("number_of_comments"),
    )
)

# pk lookups
print(Blog.objects.get(pk=14))
print(Blog.objects.get(pk=14))
print(Blog.objects.get(pk=14))
print(Blog.objects.filter(pk__in=[1, 4, 7]))
print(Blog.objects.filter(pk__gt=14))
print(Entry.objects.filter(blog__pk=3))
print(Entry.objects.filter(blog__pk=3))
print(Entry.objects.filter(blog__pk=3))

# LIKE escaping
print(Entry.objects.filter(headline__contains="%"))

# QuerySet caching
print([e.headline for e in Entry.objects.all()])
print([e.pub_date for e in Entry.objects.all()])

queryset = Entry.objects.all()
print([p.headline for p in queryset])
print([p.pub_date for p in queryset])

queryset = Entry.objects.all()
print(queryset[0])
print(queryset[0])

queryset = Entry.objects.all()
print([entry for entry in queryset])
print(queryset[0])
print(queryset[0])
