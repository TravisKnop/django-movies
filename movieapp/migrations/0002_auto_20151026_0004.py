# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='moviename',
        ),
        migrations.AlterField(
            model_name='movie',
            name='timestamp',
            field=models.IntegerField(),
        ),
    ]
