from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField(max_length=50, unique=True)
    name = models.CharField(max_length=50)


class Billing(models.Model):
    tenant_id = models.IntegerField(max_length=10, unique=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    current_amount = models.IntegerField(max_length=50)
    date = models.DateField()


