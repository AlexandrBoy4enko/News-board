import django
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=35)


class Article(models.Model):
    pub_date = models.DateField(default=django.utils.timezone.now)
    author = models.ForeignKey(Author, null=True, default=None, on_delete=models.DO_NOTHING)
    heading = models.CharField(max_length=255)
    content = models.TextField(default=None)
