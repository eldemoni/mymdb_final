# Generated by Django 3.0.2 on 2020-03-04 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
                ('picture', models.URLField(null=True)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
                ('picture', models.URLField(null=True)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese el nombre del género.', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Nombre de la película.', max_length=200)),
                ('poster', models.URLField(null=True)),
                ('trailer', models.URLField(null=True)),
                ('summary', models.TextField(help_text='Ingrese una breve descripción de la película.', max_length=1000)),
                ('release_date', models.DateField(null=True)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Director')),
                ('genre', models.ManyToManyField(help_text='Seleccione un genero para esta película', to='catalog.Genre')),
                ('saved', models.ManyToManyField(blank=True, related_name='fav_movies', to=settings.AUTH_USER_MODEL)),
                ('stars', models.ManyToManyField(help_text='Ingrese los actores principales', to='catalog.Actor')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='WhatIf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_if', models.TextField(max_length=500)),
                ('by', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Movie')),
            ],
            options={
                'ordering': ['movie'],
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Nombre de la serie.', max_length=200)),
                ('poster', models.URLField(null=True)),
                ('trailer', models.URLField(null=True)),
                ('summary', models.TextField(help_text='Ingrese una breve descripción de la película.', max_length=1000)),
                ('release_date', models.DateField(null=True)),
                ('episodes', models.IntegerField(null=True)),
                ('director', models.ManyToManyField(to='catalog.Director')),
                ('genre', models.ManyToManyField(help_text='Seleccione un genero para esta película', to='catalog.Genre')),
                ('saved', models.ManyToManyField(blank=True, related_name='fav_series', to=settings.AUTH_USER_MODEL)),
                ('stars', models.ManyToManyField(help_text='Ingrese los actores principales', to='catalog.Actor')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
