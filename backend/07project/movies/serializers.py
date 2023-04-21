from rest_framework import serializers
from .models import Actor, Movie, Review


# actor 리스트 조회
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "name")

# movie 데이터에서  title만 가져오는 serializer 
class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title",)

# 
class ActorSerializer(serializers.ModelSerializer):
    movies = TitleSerializer(many=True, read_only=True)
    print(movies)
    class Meta:
        model = Actor
        fields = ("id", "movies", "name",)


# 무비의 이름
class Movie_addserializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("name",)

# 리뷰 내용
class Movie_reviewaddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("title", "content",)


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "overview",)

class MovieSerializer(serializers.ModelSerializer):
    actors = Movie_addserializer(many=True, read_only=True)
    review_set = Movie_reviewaddSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ("id", "actors", "review_set", "title", "overview", "release_date", "poster_path",)


class Review_titleAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title",)

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("title", "content",)

class ReviewSerializer(serializers.ModelSerializer):
    movie = Review_titleAddSerializer(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"

class Movie_reviewcreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
        

