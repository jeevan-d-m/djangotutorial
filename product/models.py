from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField()

class Category(models.Model):
    name = models.CharField()
    parent_category_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField()
    ratings = models.SmallIntegerField()
    price = models.BigIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
