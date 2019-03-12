from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from purchases.serializers import PurchaseSerializer
from purchases.models import Purchase


class PurchaseViewSet(ModelViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Purchase.objects.all().order_by('-purchase_date')
    serializer_class = PurchaseSerializer
