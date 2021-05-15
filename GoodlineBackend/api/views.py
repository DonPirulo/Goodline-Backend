from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Billing
from rest_framework import generics, status
from django.http import JsonResponse
from .serializers import BillingSerializer



class GetBillingList(generics, ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

class GetBilling(APIView):
    serializer_class = BillingSerializer

    def get(self, request, format=None):
        tenant_id = request.GET.get(self.tenant_id)
        if tenant_id != None:
            billing = Billing.objects.filter(tenant_id=tenant_id)
            data = BillingSerializer(billing.data)

        
        