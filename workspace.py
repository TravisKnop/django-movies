import pandas as pd
from movieapp.models import Movie, Rater, Rating


def load_movie(apps, schema_editor):
    movie_df = pd.read_csv("~/Downloads/ml-100k/u.item", sep='|', encoding="ISO-8859-1",
                           names=["Movie_ID", "Movie", "Released", "todelete", "imdb_url", "unknown", "action",
                                  "adventure", "animation", "childrens", "comedy", "crime", "documentary", "drama",
                                  "fantasy", "film_noir", "horror", "musical", "mystery", "romance", "scifi",
                                  "thriller", "war", "western"])

    for row in movie_df.iterrows():
        movie_id = row[1].Movie_ID
        movie = row[1].Movie
        released = row[1].Released
        Movie.objects.create(id=movie_id, title=movie, released=released)


def load_rater(apps, schema_creation):
    rater_df = pd.read_csv("~/Downloads/ml-100k/u.user", sep='|', names=["user_id", 'age', "gender", "occupation", "zipcode"])

    for row in rater_df.iterrows():
        rater_id = row[1].user_id
        age = row[1].age
        gender = row[1].gender
        occupation = row[1].occupation
        zipcode = row[1].zipcode
        Rater.objects.create(id=rater_id, age=age, gender=gender, occupation=occupation, zipcode=zipcode)


def load_data(apps, schema_editor):
    ratings_df = pd.read_table("~/Downloads/ml-100k/u.data", names=["rater", "movie", "rating", "datetime"])
    Rating = apps.get_model("movieapp", "Rating")
    Movie = apps.get_model("movieapp", "Movie")
    Rater = apps.get_model("movieapp", "Rater")
    for row in ratings_df.iterrows():
        rating = row[1].rating
        movie = row[1].movie
        rater = row[1].rater
        Rating.objects.create(rated_movie=Movie.objects.get(id=movie), rater=Rater.objects.get(id=rater), rating=rating)

