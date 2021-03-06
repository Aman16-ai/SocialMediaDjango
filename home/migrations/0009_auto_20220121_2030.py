# Generated by Django 3.1.5 on 2022-01-21 15:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_posts_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_likes', to='home.UserProfile'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 21, 20, 30, 37, 704521)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='user_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userprofile'),
        ),
    ]
