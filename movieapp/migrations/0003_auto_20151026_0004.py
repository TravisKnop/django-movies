# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pandas as pd
from django.db import migrations
from movieapp.models import Data
from movieapp.models import Rater


def add_data(apps, schema_editor):
    df = pd.read_table("ml_100k/u.data", names=["userid", "itemid", "rating", "timestamp"])
    Data = apps.get_model('movieapp', "Data")

    for index, row in df.iterrows():
        userid = row['userid']
        itemid = row['itemid']
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
