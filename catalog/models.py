from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User



class Genre(models.Model):
    '''
    Modelo que representa un género cinematográfico.
    '''
    name = models.CharField(max_length=200, help_text='Ingrese el nombre del género.')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genres', args=[str(self.id)])

    class Meta:
        ordering = ['name']


class Movie(models.Model):
    '''
    Modelo que representa una película.
    '''
    title = models.CharField(max_length=200, help_text='Nombre de la película.')

    poster = models.URLField(null=True)

    trailer = models.URLField(null=True)

    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que una película tiene un solo director, pero el mismo director puede haber dirigido varias peliculas.

    stars = models.ManyToManyField('Actor', help_text='Ingrese los actores principales')

    summary = models.TextField(max_length=1000, help_text='Ingrese una breve descripción de la película.')

    release_date = models.DateField(null=True)

    genre = models.ManyToManyField(Genre, help_text="Seleccione un genero para esta película")

    saved = models.ManyToManyField(User, related_name='fav_movies', blank=True)

    def __str__(self):
        '''
        String que representa al objeto Movie
        '''
        return self.title

    def get_absolute_url(self):
        '''
        Devuelve el URL a una instancia particular de Movie
        '''
        return reverse('movie-detail', args=[str(self.id)])
    
    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

    class Meta:
        ordering = ['title']


class Series(models.Model):
    '''
    Modelo que representa una serie.
    '''
    title = models.CharField(max_length=200, help_text='Nombre de la serie.')

    poster = models.URLField(null=True)

    trailer = models.URLField(null=True)

    director = models.ManyToManyField('Director')

    stars = models.ManyToManyField('Actor', help_text='Ingrese los actores principales')

    summary = models.TextField(max_length=1000, help_text='Ingrese una breve descripción de la película.')

    release_date = models.DateField(null=True)

    episodes = models.IntegerField(null=True)

    genre = models.ManyToManyField(Genre, help_text="Seleccione un genero para esta película")

    saved = models.ManyToManyField(User, related_name='fav_series', blank=True)

    def __str__(self):
        '''
        String que representa al objeto Series
        '''
        return self.title

    def get_absolute_url(self):
        '''
        Devuelve el URL a una instancia particular de Series
        '''
        return reverse('series-detail', args=[str(self.id)])
        
    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

    class Meta:
        ordering = ['title']


class Director(models.Model):
    """
    Modelo que representa un director
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    picture = models.URLField(null=True)
    
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un director.
        """
        return reverse('director-detail', args=[str(self.id)])

    def __str__(self):
        """
        String para representar el Objeto Director
        """
        return '%s, %s' % (self.last_name, self.first_name)
    
    class Meta:
        ordering = ['last_name']


class Actor(models.Model):
    """
    Modelo que representa un actor
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    picture = models.URLField(null=True)
    
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un actor.
        """
        return reverse('actor-detail', args=[str(self.id)])
    
    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
    
    class Meta:
        ordering = ['last_name']


class WhatIf(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    what_if = models.TextField(max_length=500)
    by = models.ForeignKey(User, on_delete=models.SET_NULL, default=1, null=True, blank=True)
    likes= models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes= models.ManyToManyField(User, related_name='dislikes', blank=True)
    
    def get_absolute_url(self):
        return reverse('what-if-detail', args=[str(self.id)])

    class Meta:
       ordering = ['movie']


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    mail = models.EmailField()

    def __unicode__(self):
        return self.user.username






