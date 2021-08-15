from rest_framework import serializers
from django.db.models import fields
from app1.models import Customer, Product, Cart, OrderPlaced

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user','name','locality','city','zipcode','state']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title','selling_price','discounted_price','description','brand','category','product_image']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user','product','quantity']

class OrderPlacedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user','customer','product','quantity','ordered_date','status']