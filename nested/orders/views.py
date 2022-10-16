from django.shortcuts import render

from .models import Customer, Order
from orders.serializer import OrderSerializer, CustomerSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CustromerListView(generics.ListAPIView):
    querryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = StandardResultsSetPagination


class CustromerDetailView(generics.RetrieveUpdateDestroyAPIView):
    querryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderListView(generics.ListAPIView):
    querryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = LargeResultsSetPagination


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    querryset = Order.objects.all()
    serializer_class = OrderSerializer
