from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PurchaseSerializer
from .models import Purchase


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by('-purchase_date')
    serializer_class = PurchaseSerializer
