from django.db import models
from django.db.models import Model, IntegerField
from django.utils.timezone import now


class Author(Model):
    id = IntegerField(primary_key=True)
    name = models.CharField(max_length=35)

    def __repr__(self):
        return f"#{self.id} {self.name}"


class Article(models.Model):
    pub_date = models.DateField(default=now)
    author = models.ForeignKey(Author, null=True, default=None, on_delete=models.DO_NOTHING)
    heading = models.CharField(max_length=255)
    content = models.TextField(default=None)
