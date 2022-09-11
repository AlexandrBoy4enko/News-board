from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, CreateModelMixin, \
    UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from news_feed.models import Article
from news_feed.serializers import ArticleSerializer


class ArticleViewSet(ListModelMixin,
                     RetrieveModelMixin,
                     CreateModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     GenericViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
