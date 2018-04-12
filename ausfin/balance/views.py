from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import BalanceUpdate
from .serializers import BalanceUpdateSerializer


class BalanceUpdateViewSet(ModelViewSet):
    queryset = BalanceUpdate.objects.all()
    serializer_class = BalanceUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
