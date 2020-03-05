from django.contrib import admin
from .models import Actor, Director, Genre, Movie, Series, WhatIf, Profiles

admin.site.register(Genre)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'picture')
        }),
        ('Birth-Death', {
            'fields': (('date_of_birth', 'date_of_death'),)
        }),
    )
admin.site.register(Actor, ActorAdmin)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'picture')
        }),
        ('Birth-Death', {
            'fields': (('date_of_birth', 'date_of_death'),)
        }),
    )
admin.site.register(Director, DirectorAdmin)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_date', 'display_genre')
    list_filter = ('genre', 'director')
    fieldsets = (
        (None, {
            'fields': ('title', 'genre', 'poster', 'trailer')
        }),
        ('Extra Info', {
            'fields': (('director', 'stars', 'release_date', 'saved', 'summary'),)
        }),
    )

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'display_genre', 'episodes')
    list_filter = ('genre', 'director',)
    fieldsets = (
        (None, {
            'fields': ('title', 'genre', 'poster', 'trailer')
        }),
        ('Extra Info', {
            'fields': (('director', 'stars', 'release_date', 'saved', 'episodes','summary'),)
        }),
    )

@admin.register(WhatIf)
class WhatIfAdmin(admin.ModelAdmin):
    list_display = ('movie',)
    fieldsets = (
        (None, {
            'fields': ('movie', 'what_if', 'by', 'likes', 'dislikes')
        }),
    )

@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user',)
    fieldsets = (
        (None, {
            'fields': ('user', 'mail')
        }),
    )
