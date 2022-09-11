from rest_framework.serializers import ModelSerializer

from news_feed.models import Article, Author


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
