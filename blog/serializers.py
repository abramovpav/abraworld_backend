from django.forms import widgets
from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'create_date', 'update_date', 'author')
