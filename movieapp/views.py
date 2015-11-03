from django.views.generic import View, CreateView, ListView, DetailView
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from movieapp.models import Movie, Rater, Rating

# Create your views here.


def home_view(request):
    return render_to_response(template_name='base.html', context={})


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


class MovieRating(CreateView):
    model = Rating
    fields = ['rater', 'rated_movie', 'rating']
    success_url = '/'

"""class DataListView(ListView):
    model = Movie
    template_name = "base.html"

    def data(self):
        context = {}
        raterid = request.GET.get("raterid")
        movieid = request.GET.get("movieid")
        rating = request.GET.get("rating")
        timestamp = request.GET.get("timestamp")
        return render_to_response(template_name="movieapp/data.html", context=context)

"""

#def index_view(request):
    #movies = sorted(Movie.objects.all(), key=lambda x x.avg_rating, reverse=True)
    #context = {'movies': movies [0:20]}


""" class MovieListView(ListView):
        model = Movie
        template_name = "data.html"
"""