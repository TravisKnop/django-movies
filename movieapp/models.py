from django.db import models


# Create your models here.

class Data(models.Model):
    userid = models.IntegerField()
    itemid = models.IntegerField()
    rating = models.IntegerField()
    timestamp = models.IntegerField()
    #moviename = models.CharField(max_length=100)
    #def make_avg_rating(self):
        #avg_rating = self.rating_set.aggregate(Avg('rating))
        #return avg_rating['rating__avg']

    #avg_rating = property(make_avg_rating)


# renamed from u.user:
class Rater(models.Model):
    userid = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    zipcode = models.IntegerField()

