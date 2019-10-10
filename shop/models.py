from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=255)


# Create your models here.
# Category has many products
class Product (models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
