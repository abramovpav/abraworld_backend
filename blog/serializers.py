from rest_framework import serializers

from blog.models import Article
from profiles.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'create_date', 'update_date', 'author')
        read_only_fields = ('create_date', 'update_date')
