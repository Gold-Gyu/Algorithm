from rest_framework import serializers
from .models import Article, Comment

# article 모델에서 보내줄 것들을 직렬화 한다.

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


# 코맨트 serializer
class CommentSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop("article", None)
        return rep

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article",) # literable 반복가능한


class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Article안에 comment라는 것의 직렬화가 필요함 =>  
    # why read only 수정이 불가능한 읽기전용필드를 만든다
    comment_set = CommentSerializer(many=True, read_only=True)
    # 모델에 없는 필드를 추가해주는 것
    comment_count = serializers.IntegerField(source="comment_set.count") # 댓글의 갯수를 세서 출력한다.
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["comment"] = rep.pop("comment_set", []) # comment_set이 있으면 그것을 보내고 없으면 [] 빈리스트를 보낸다.
        return rep

    class Meta:
        model = Article
        fields = "__all__"