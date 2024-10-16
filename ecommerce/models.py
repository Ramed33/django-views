from django.db import models

# Create your models here.
class ProductModel(models.Model):
    title = models.TextField()
    price = models.FloatField()
    description = models.TextField(max_length=500, blank=False, null=True)
    seller = models.TextField(max_length=500, blank=False, null=True)
    color = models.TextField(max_length=500, blank=False, null=True)
    product_dimensions = models.TextField(max_length=500, blank=False, null=True)
