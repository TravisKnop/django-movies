# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('rated_movie', models.IntegerField()),
                ('rater', models.ForeignKey(to='movieapp.Rater')),
            ],
        ),
    ]
