from rest_framework.viewsets import ModelViewSet

from news_feed.models import Article
from news_feed.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self):
        return self.get_queryset()
