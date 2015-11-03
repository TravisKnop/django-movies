from django.db import models
import numpy as np

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    released = models.IntegerField()

    @property
    def ave_rating(self):
        return np.mean(self.rating_set.all())

    def __str__(self):
        return str(self.id)


# renamed from u.user:
class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    occupation = models.CharField(max_length=20)
    zipcode = models.IntegerField()


class Rating(models.Model):
    rating = models.IntegerField()
    rated_movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)
