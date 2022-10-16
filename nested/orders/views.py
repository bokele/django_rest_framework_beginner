from django.shortcuts import render

from .models import Customer, Order
from orders.serializer import OrderSerializer, CustomerSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

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
    # filter_backends = [DjangoFilterBackend]
    # filter_backends = [filters.OrderingFilter]
    filter_backends = [filters.SearchFilter]
    # filterset_fields = ['firstName', 'lastName', 'phone']
    # search_fields = ['^firstName', '^lastName', '^phone']
    # search_fields = ['=firstName', '=lastName', '=phone']
    # ordering_fields = ['firstName', 'lastName', 'phone']
    search_fields = ['firstName', 'lastName', 'phone']


class CustromerDetailView(generics.RetrieveUpdateDestroyAPIView):
    querryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderListView(generics.ListAPIView):
    querryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'qte']


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    querryset = Order.objects.all()
    serializer_class = OrderSerializer
