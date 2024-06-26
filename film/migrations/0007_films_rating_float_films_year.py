# Generated by Django 4.2.5 on 2023-11-29 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0006_genre_films_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='rating_float',
            field=models.FloatField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AddField(
            model_name='films',
            name='year',
            field=models.IntegerField(default=0, verbose_name='Год выпуска'),
        ),
    ]
