from django.db import models

class ZipCode(models.Model):
    code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code} - {self.city}"
