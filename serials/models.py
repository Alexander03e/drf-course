from django.db import models
from film.models import Genre,Director
# Create your models here.
class Serials(models.Model):
    title = models.CharField('Сериал', max_length=50, default='')
    subtitle =  models.TextField('Описание')
    image = models.ImageField(upload_to='static/img/', verbose_name='Изображение')
    is_favorite = models.BooleanField(default=False)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    director = models.ManyToManyField(Director, verbose_name='Режиссер')
    def __str__(self):
        return self.title

    def get_genre(self):
        return ",".join([str(p) for p in self.genre.all()])
    
    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'