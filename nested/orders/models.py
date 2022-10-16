from django.db import models

# Create your models here.


class Customer(models.Model):
    firstName = models.CharField(max_length=50, null=False,  blank=False)
    lastName = models.CharField(max_length=50, null=False,  blank=False)
    phone = models.CharField(max_length=50, null=False,  blank=False)


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, related_name='orders', on_delete=models.CASCADE)
    product = models.CharField(max_length=100, null=False,  blank=False)
    qte = models.IntegerField(default=1, null=False,  blank=False)
