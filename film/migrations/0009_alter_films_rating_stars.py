# Generated by Django 4.2.5 on 2023-11-29 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0008_rate_remove_films_rating_float_films_rating_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='rating_stars',
            field=models.ManyToManyField(to='film.rate', verbose_name='Рейтинг'),
        ),
    ]
