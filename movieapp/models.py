from django.db import models
import numpy as np

# Create your models here.

random_var = "hello"


class RatingManager(models.Manager):

    @property
    def twenty_best(self):
        top_movies = []
        for movie in Movie.objects.all():
            top_movies.append(movie)
        return sorted(top_movies, key=lambda x: x.ave_rating, reverse=True)[:20]


# from u.item:
class Movie(models.Model):
    title = models.CharField(max_length=100)
    released = models.CharField(max_length=20)

#    objects = RatingManager()
    @property
    def ave_rating(self):
        ave_score =  np.mean(self.rating_set.all().values_list('rating', flat=True))
        return "%.2f" % ave_score

    @property
    def num_ratings(self):
        return len(self.rating_set.all().values_list('rating', flat=True))

    def __str__(self):
        return str(self.id)


# renamed from u.user:
class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    occupation = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

# from u.data:
class Rating(models.Model):
    rating = models.IntegerField()
    rated_movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)
