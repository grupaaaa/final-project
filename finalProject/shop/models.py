from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    product_description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    measurement_unit = models.CharField(max_length=200,null=True)
    availability = models.BooleanField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    def __str__(self):
        return self.name

class Storage(models.Model):
    amount = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

