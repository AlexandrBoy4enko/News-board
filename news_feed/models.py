from django.db import models
from django.utils.timezone import now


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)


class Article(models.Model):
    pub_date = models.DateField(default=now)
    author = models.ForeignKey(
        to='Author',
        null=True,
        default=None,
        on_delete=models.DO_NOTHING,
        related_name='article'
    )
    heading = models.CharField(max_length=255)
    content = models.TextField(default=None)
