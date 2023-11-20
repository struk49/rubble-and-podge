from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=215)
    description = models.CharField(max_length=3000, null=True, blank=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


def __unicode__(self):
    return self.title
