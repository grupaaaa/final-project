from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.models import User
from address_form.models import ShippingAddress


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


measurement = [('Kg', 'Kg'), ('Liter', 'Liter'), ('Piece', 'Piece')]

availability_status = [('Available', 'Available'), ('Out of stock', 'Out od stock')]


class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(1), MaxValueValidator(100)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    product_description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    measurement_unit = models.CharField(max_length=20, choices=measurement)
    availability = models.CharField(max_length=20, choices=availability_status)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name



class OrderStatusChoice(models.TextChoices):
    INITIAL = 'I', 'Initial'
    ADDRESS = 'A', 'Address'
    PAYMENT = 'P', 'Payment'
    CANCELLED = 'C', 'Cancelled'
    SUCCESSED = 'S', 'Successed'


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=20, default=OrderStatusChoice.INITIAL, choices=OrderStatusChoice.choices)
    address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Ordered by: {self.customer}, at: {self.order_date} , {self.id}"





