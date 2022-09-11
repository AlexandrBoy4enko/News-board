from rest_framework.viewsets import ModelViewSet

from store.models import Article
from store.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self):
        return self.get_queryset()
