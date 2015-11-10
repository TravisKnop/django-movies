# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_auto_20151103_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='released',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(max_length=10),
        ),
    ]
