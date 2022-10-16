
from django.contrib import admin
from django.urls import path
from nested.orders.views import CustromerDetailView
from orders import views
urlpatterns = [
    path('customers/', views.CustromerListView.as_view())
    path('customers/<int:pk>', views.CustromerDetailView.as_view())
    path('orders/', views.OrderListView.as_view())

    path('orders/<int:pk>', views.OrderDetailView.as_view())
]
