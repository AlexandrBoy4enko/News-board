from rest_framework.serializers import ModelSerializer

from store.models import news

class newssSerializer(ModelSerializer):
    class Meta:
        model=news
        fields='__all__'
