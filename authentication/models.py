from django.db import models
from film.models import Films
from serials.models import Serials
# from django.contrib.auth.models import AbstractUser

# # Create your models here.

# class User(AbstractUser):
#   email = models.EmailField(verbose_name='Email', unique = True)
  
#   REQUIRED_FIELDS = ['email']

class User(models.Model):
  first_name = models.CharField('Имя', max_length=50, default='')
  last_name = models.CharField('Фамилия', max_length=50, default='')
  username = models.CharField('username', max_length=20, default='')
  email = models.EmailField('Email', default='')
  favorite_films=models.ManyToManyField(Films, related_name='понравилось', blank=True, null=True)
  favorite_serials=models.ManyToManyField(Serials, related_name='понравилось', blank=True, null=True)

  def __str__(self):
    return self.email
  
  class Meta: 
    verbose_name = 'Клиент'
    verbose_name_plural ='Клиенты'
    
