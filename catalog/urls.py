from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^movies/$', views.MovieListView.as_view(), name='movies'),
    url(r'^movie/(?P<pk>\d+)$', views.MovieDetailView.as_view(), name='movie-detail'),
    url(r'^movie/(?P<pk>\d+)/update/$', views.SavedMovieUpdate.as_view(), name='saved-movie-update'),

    url(r'^series/$', views.SeriesListView.as_view(), name='series'),
    url(r'^series/(?P<pk>\d+)$', views.SeriesDetailView.as_view(), name='series-detail'),
    url(r'^series/(?P<pk>\d+)/update/$', views.SavedSeriesUpdate.as_view(), name='saved-series-update'),

    url(r'^directors/$', views.DirectorListView.as_view(), name='directors'),
    url(r'^director/(?P<pk>\d+)$', views.DirectorDetailView.as_view(), name='director-detail'),

    url(r'^actors/$', views.ActorListView.as_view(), name='actors'),
    url(r'^actor/(?P<pk>\d+)$', views.ActorDetailView.as_view(), name='actor-detail'),

    url(r'^mymovies/$', views.SavedMoviesByUserListView.as_view(), name='my-movies'),
    url(r'^myseries/$', views.SavedSeriesByUserListView.as_view(), name='my-series'),

    url(r'whatif/$', views.WriteWhatIfView.as_view(), name='what-if'),
    url(r'whatifs/$', views.WhatIfListView.as_view(), name='what-ifs'),
    url(r'whatif/(?P<pk>\d+)$', views.WhatIfDetailView.as_view(), name='what-if-detail'),
    url(r'whatif/(?P<pk>\d+)/update/$', views.WhatIfUpdateView.as_view(), name='what-if-update'),

    url(r'^register/$', views.Register.as_view(), name='register'),

    url(r'^search/$', views.SearchView.as_view(), name='search'),

    url(r'^genres/$', views.GenreListView.as_view(), name='genres'),
    url(r'^genre/(?P<pk>\d+)$', views.GenreDetailView.as_view(), name='genre-detail'),

]