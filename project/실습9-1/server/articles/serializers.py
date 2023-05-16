from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    author_id = serializers.CharField(source='author.id', read_only=True)
    author_username = serializers.CharField(source='author.username', read_only=True)
    # author2 = serializers.CharField(source='author', read_only=True)
    class Meta:
        model = Article
        
        fields = ('id', 'title', 'content', 'author_id', 'author_username', 'updated_at')