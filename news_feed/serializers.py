from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from news_feed.models import Article, Author


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    author = CharField(source="author.name")

    def create(self, validated_data):
        author, _ = Author.objects.get_or_create(name=validated_data['author']['name'])
        instance = Article.objects.create(
            pub_date=validated_data['pub_date'],
            author=author,
            heading=validated_data['heading'],
            content=validated_data['content']
        )
        instance.save()
        return instance


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', ]
