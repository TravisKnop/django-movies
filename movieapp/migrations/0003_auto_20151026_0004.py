# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pandas as pd
from django.db import migrations
from movieapp.models import Movie
from movieapp.models import Rater


def add_data(apps, schema_editor):
    df = pd.read_table("ml_100k/u.data", names=["raterid", "movieid", "rating", "timestamp"])
    Data = apps.get_model('movieapp', "Movie")

    for index, row in df.iterrows():
        userid = row['raterid']
        itemid = row['movieid']
        rating = row['rating']
        timestamp = row['timestamp']
        Data.objects.create(userid=userid, itemid=itemid, rating=rating, timestamp=timestamp)


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        (migrations.RunPython(add_data)),
        ]
