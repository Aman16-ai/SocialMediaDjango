# Generated by Django 4.0.1 on 2022-01-20 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 20, 21, 18, 31, 555600)),
        ),
    ]
