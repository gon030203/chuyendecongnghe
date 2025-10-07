from django.db import models
from geography.models import ZipCode
import uuid
from django.utils.text import slugify

# Ví dụ cơ bản
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # Model method: row-level logic
    def baby_boomer_status(self):
        """Trả về trạng thái generation của người"""
        if not self.birth_date:
            return "Unknown"
        if self.birth_date < date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    # Property
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    

# Ví dụ có quan hệ
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name="albums")
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.artist})"


# Ví dụ choices
class Runner(models.Model):
    class MedalType(models.TextChoices):
        GOLD = "G", "Gold"
        SILVER = "S", "Silver"
        BRONZE = "B", "Bronze"

    name = models.CharField(max_length=60)
    medal = models.CharField(max_length=1, choices=MedalType.choices, blank=True)

    def __str__(self):
        return f"{self.name} - {self.get_medal_display()}"


# Ví dụ UUID làm primary key
class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)


from django.db import models
from datetime import date



# Many-to-One (ForeignKey)
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.manufacturer})"



# Many-to-Many 
class PersonBand(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(PersonBand, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(PersonBand, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.person} in {self.group}"



# One-to-One
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} - {self.address}"


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    zip_code = models.ForeignKey(
        ZipCode,
        on_delete=models.SET_NULL,  # nếu ZipCode bị xóa, để null
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Restaurant: {self.place.name}"

class Ox(models.Model):
    horn_length = models.IntegerField()
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["horn_length"]          # sắp xếp theo horn_length mặc định
        verbose_name = "Ox"                 # tên hiển thị số ít
        verbose_name_plural = "Oxen"        # tên hiển thị số nhiều
        db_table = "farm_ox"                # đặt tên bảng trong database
        unique_together = [["name", "horn_length"]]  # kết hợp duy nhất

# Override save()
class Blog(models.Model):
    name = models.CharField(max_length=100)
    slug = models.TextField()
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        # Tự động tạo slug từ name
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)  # nhớ gọi super() để lưu vào DB

# Abstract Base Class
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True  # Không tạo bảng trong DB

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} ({self.home_group})"

# Proxy Model
class PersonProxy(Person):
    class Meta:
        proxy = True
        ordering = ["last_name"]  # thay đổi default ordering

    def do_something(self):
        return f"{self.full_name} is doing something!"