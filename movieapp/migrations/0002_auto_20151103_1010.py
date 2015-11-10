# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from workspace import load_rater, load_data, load_movie

class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_movie),

        migrations.RunPython(load_rater),

        migrations.RunPython(load_data),
]
