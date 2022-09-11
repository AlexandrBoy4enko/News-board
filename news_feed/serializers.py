from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from news_feed.models import Article, Author


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    author = CharField(source="author.name")


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', ]

    def __repr__(self):
        return f"#{self.id} {self.name}"
