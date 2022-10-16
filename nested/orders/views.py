from django.shortcuts import render

from .models import Customer, Order
from orders.serializer import OrderSerializer, CustomerSerializer
from rest_framework import generics

# Create your views here.


class CustromerListView(generics.ListAPIView):
    querryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustromerDetailView(generics.RetrieveUpdateDestroyAPIView):
    querryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderListView(generics.ListAPIView):
    querryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    querryset = Order.objects.all()
    serializer_class = OrderSerializer
