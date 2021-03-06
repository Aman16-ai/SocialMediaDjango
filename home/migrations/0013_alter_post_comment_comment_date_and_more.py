# Generated by Django 4.0.1 on 2022-01-29 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_post_comment_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_comment',
            name='comment_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 29, 21, 18, 47, 951752)),
        ),
        migrations.AlterField(
            model_name='post_comment',
            name='comment_likes',
            field=models.ManyToManyField(blank=True, null=True, to='home.UserProfile'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 29, 21, 18, 47, 951752)),
        ),
    ]
