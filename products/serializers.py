from rest_framework import serializers
from .models import Product, Sale

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'name', 'description', 'sku', 'stock')

class ProductDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'name', 'price', 'sku', 'stock')

class SaleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('quantity', 'product' )

    def create(self, validate_data):
        print(validate_data)
        quantity = validate_data['quantity']
        product = validate_data['product']
        print(product)

        if product.stock >= quantity:
            total = product.price * quantity
            newSale = Sale(product=product,  total_price=total, quantity=quantity)
            product.stock = product.stock - quantity
            product.save()
            newSale.save()
            validate_data['total_price'] = total
        else:
            validate_data['total_price'] = 0
        return validate_data

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Sale
        fields = '__all__'

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =  ('name', 'price', 'description', 'sku', 'stock')