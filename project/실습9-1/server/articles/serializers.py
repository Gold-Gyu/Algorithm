from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.id', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    # author2 = serializers.CharField(source='author', read_only=True)
    class Meta:
        model = Article
        
        fields = ('id', 'title', 'content', 'user_id', 'user_username', 'updated_at')