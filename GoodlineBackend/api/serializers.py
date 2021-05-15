from rest_framework import serializers
from .models import Billing

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ('tenant_id', 'customer_id', 'current_amount', 'date')