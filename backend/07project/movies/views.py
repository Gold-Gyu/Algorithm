from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Actor, Movie, Review
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, Movie_reviewcreateSerializer
# Create your views here.

# 전체 목록 조회하기
@api_view(['GET'])
def actor_list(request):
    if request.method == "GET":
        actors = Actor.objects.all()
        # print(actors)
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actors = get_object_or_404(Actor, pk = actor_pk)
    if request.method == "GET":
        serializer = ActorSerializer(actors)
        return Response(serializer.data)
    
@api_view(['GET'])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def movie_detail(request, movie_pk):
    movies = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "GET":
        serializer = MovieSerializer(movies)
        return Response(serializer.data)
    

@api_view(["GET", "POST"])
def review_list(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    reviews = get_object_or_404(Review, pk = review_pk)
    if request.method == "GET":
        serializer = ReviewSerializer(reviews)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ReviewSerializer(reviews, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == "DELETE":
        reviews.delete()
        review_ans = {"delete" : f"review {review_pk} is deleted"}
        return Response(review_ans)
    
@api_view(["GET","POST"])
def create_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)

    if request.method == "GET":
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
