from django.views.generic import CreateView, ListView, DetailView
from django.http import HttpResponse
from django.shortcuts import render_to_response
from movieapp.models import Movie, Rater, RatingManager

# Create your views here.


def home_view(request):
    return render_to_response(template_name='index.html',
                              context={"twenty_best": RatingManager.twenty_best})


class MovieList(ListView):
    model = Movie
    template = "movie_list.html"


class MovieDetail(DetailView):
    model = Movie
    template = "movie_detail.html"


class RaterList(ListView):
    model = Rater
    template = "rater_list.html"


class RaterDetail(DetailView):
    model = Rater
    template = "movie_detail.html"


# class MovieRating(CreateView):
#    model = Rating
#    fields = ['rater', 'rated_movie', 'rating']
#    success_url = '/'


# def index_view(request):
    # movies = sorted(Movie.objects.all(), key=lambda x x.avg_rating, reverse=True)
    # context = {'movies': movies [0:20]}
