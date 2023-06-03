from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    class Meta:
        ordering = ['name', 'price']
        # db_table = 'tech_products'
        # verbose_name_plural = 'products'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_received = models.DateTimeField(auto_now_add=True)
    has_additional_guarantee = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

    # @property
    # def description_short(self) -> str:
    #     if len(self.description) < 50:
    #         return self.description
    #     return self.description[:50] + '...'

    def __str__(self) -> str:
        return f'Product {self.name} with id={self.id} for ${self.price} --> {self.quantity} items. {self.description}'


class Order(models.Model):
    delivery_address = models.TextField(null=False, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')
