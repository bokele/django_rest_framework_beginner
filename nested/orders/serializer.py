from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Customer, Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(read_only=True, many=True)

    class Meta:
        model = Customer
        fields = "__all__"
