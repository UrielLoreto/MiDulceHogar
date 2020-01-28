from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=10)
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=300)
    stock = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='products')
    quantity = models.IntegerField(null=False)
    total_price = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)