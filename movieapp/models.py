from django.db import models
import numpy as np
import pandas as pd

# Create your models here.


class Movie(models.Model):
    raterid = models.IntegerField()
    movieid = models.IntegerField()
    rating = models.IntegerField()
    timestamp = models.IntegerField()

    @property
    def ave_rating(self):
        return np.mean(self.rating_set.all())

    def __str__(self):
        return str(self.id)


# renamed from u.user:
class Rater(models.Model):
    raterid = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    zipcode = models.IntegerField()


class Rating(models.Model):
    rating = models.IntegerField()
    rated_movie = models.IntegerField()
    rater = models.ForeignKey(Rater)
