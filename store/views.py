from rest_framework.viewsets import ModelViewSet

from store.models import news
from store.serializers import newssSerializer

class newsViewSet(ModelViewSet):
    queryset = news.objects.all()
    serializer_class = newssSerializer
