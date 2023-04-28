from django.shortcuts import render
from django.views.decorators.http import require_safe
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Genre

# Create your views here.



@require_safe
def index(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        print(movies[0].genres.all())
        context = {
            'movies' : movies,
        }
        return render(request, 'movies/index.html', context)

@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    genres = Genre.objects.filter(movie=movie)
    context = {
        "movie" : movie,
        "genres" : genres,

    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    # movies = Movie.objects.all()
    recommends = Movie.objects.order_by("-popularity")[:10]
    context = {
        # "movies" : movies,
        "recommends" : recommends,
    }
    return render(request, 'movies/recommended.html', context)