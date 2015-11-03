import pandas as pd
from movieapp.models import Movie, Rater, Rating


def load_data(apps, schema_editor):
    ratings_df = pd.read_table("~/Downloads/ml-100k/u.data", names=["raterid", "movieid", "rating", "datetime"])
#    Review = apps.get_model("movieapp", "Review")
#    Movie = apps.get_model("movieapp", "Movie")
#    Rater = apps.get_model("movieapp", "Rater")
    for row in ratings_df.iterrows():
            rating = row[1].rating
            movieid = row[1].movieid
            raterid = row[1].raterid
            Rating.objects.create(movieid=Movie.objects.get(movieid=movieid), raterid=Rater.objects.get(raterid=raterid), rating=rating)

def load_movie(apps, schema_editor):
    movie_df = pd.read_csv("~/Downloads/ml-100k/u.item", sep='|', encoding="ISO-8859-1",
                           names=["movieid", "movie", "released", "todelete", "imdb_url", "unknown", "action",
                                  "adventure", "animation", "childrens", "comedy", "crime", "documentary", "drama",
                                  "fantasy", "film_noir", "horror", "musical", "mystery", "romance", "scifi",
                                  "thriller", "war", "western"])

    for row in movie_df.iterrows():
        movieid = row[1].Movie_ID
        movie = row[1].Movie
        released = row[1].released
        Movie.objects.create(movieid=movieid, movietitle=movie, released=released)

def load_rater(apps, schema_creation):
    rater_df = pd.read_csv("~/Downloads/ml-100k/u.user", sep='|', names=["raterid", 'age', "gender", "occupation", "zipcode"])

    for row in rater_df.iterrows():
        raterid = row[1].raterid
        age = row[1].age
        gender = row[1].gender
        occupation = row[1].occupation
        zipcode = row[1].zipcode
        Rater.objects.create(raterid=raterid, age=age, gender=gender, occupation=occupation, zipcode=zipcode)