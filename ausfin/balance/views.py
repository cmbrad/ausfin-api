from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import BalanceEvent
from .serializers import BalanceEventSerializer


class BalanceEventViewSet(ModelViewSet):
    queryset = BalanceEvent.objects.all()
    serializer_class = BalanceEventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
