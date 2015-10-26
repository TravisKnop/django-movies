from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from movieapp.models import Data, Rater

# Create your views here.


class IndexView(View):

    def index(self):
        HttpResponse("hello?")


class DataListView(ListView):
    model = Data
    template_name = "base.html"

    def data(self):
        context = {}
        userid = request.GET.get("userid")
        itemid = request.GET.get("itemid")
        rating = request.GET.get("rating")
        timestamp = request.GET.get("timestamp")
        return render_to_response(template_name="movieapp/data.html", context=context)


# renamed from u.user:
# class Rater(models.Model):
#    userid = models.CharField(max_length=20)
#    age = models.IntegerField()
#    gender = models.CharField(max_length=1)
#    occupation = models.CharField(max_length=20)
#    zipcode = models.IntegerField()

#def index_view(request):
    #movies = sorted(Data.objects.all(), key=lambda x x.avg_rating, reverse=True)
    #context = {'movies': movies [0:20]}


""" class MovieListView(ListView):
        model = Data
        template_name = "data.html"
"""