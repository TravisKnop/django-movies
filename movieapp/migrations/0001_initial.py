# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('raterid', models.IntegerField()),
                ('movieid', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('raterid', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('occupation', models.CharField(max_length=20)),
                ('zipcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('rating', models.IntegerField()),
                ('rated_movie', models.IntegerField()),
                ('rater', models.ForeignKey(to='movieapp.Rater')),
            ],
        ),
    ]
