from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    img = models.ImageField()
    role = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    class Meta():pass