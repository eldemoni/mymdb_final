from django.shortcuts import render
from .models import Actor, Director, Genre, Movie, Series, WhatIf, Profiles
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, TemplateView, FormView, UpdateView, RedirectView
from django.urls import reverse, reverse_lazy
from .forms import UserForm
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required




def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_movies = Movie.objects.all().count()
    num_series = Series.objects.all().count()
    num_directors = Director.objects.all().count()
    num_actors = Actor.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    #Renderiza la plantilla HTML index.html con los datos en la variable context
    return render(
        request,
        'index.html',
        context={'num_movies':num_movies,'num_series':num_series,'num_directors':num_directors,'num_actors':num_actors,
        'num_visits':num_visits}
    )


class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 25

class MovieDetailView(generic.DetailView):
    model = Movie


class SeriesListView(generic.ListView):
    model = Series
    paginate_by = 10

class SeriesDetailView(generic.DetailView):
    model = Series


class DirectorListView(generic.ListView):
    model = Director
    paginate_by = 25

class DirectorDetailView(generic.DetailView):
    model = Director


class ActorListView(generic.ListView):
    model = Actor
    paginate_by = 50

class ActorDetailView(generic.DetailView):
    model = Actor


class GenreListView(generic.ListView):
    model = Genre

class GenreDetailView(generic.DetailView):
    model = Genre


class SavedMoviesByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing movies saved by current user. 
    """
    model = Movie
    template_name ='catalog/saved_movies_list_user.html'
    paginate_by = 25
    
    def get_queryset(self):
        return Movie.objects.filter(saved=self.request.user).order_by('title')

class SavedMovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ['saved']

    

class SavedSeriesByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing series saved by current user. 
    """
    model = Series
    template_name ='catalog/saved_series_list_user.html'
    paginate_by = 25
    
    def get_queryset(self):
        return Series.objects.filter(saved=self.request.user).order_by('title')

class SavedSeriesUpdate(LoginRequiredMixin, UpdateView):
    model = Series
    fields = ['saved']


class WriteWhatIfView(generic.CreateView):
    model = WhatIf
    fields = '__all__'
    template_name = 'catalog/what_if.html'
    def get_success_url(self):
        return reverse('what-ifs')

class WhatIfListView(generic.ListView):
    model = WhatIf

class WhatIfDetailView(generic.DetailView):
    model = WhatIf

class WhatIfUpdateView(UpdateView):
    model = WhatIf
    fields = ['likes', 'dislikes']


class Register(FormView):
    template_name = 'registration/register.html'
    form_class = UserForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        usuario = form.save()
        profile = Profiles()
        profile.user = usuario
        profile.mail = form.cleaned_data['mail']
        profile.save()
        return super(Register, self).form_valid(form)
        

class SearchView(TemplateView):
    def get(self, request, *args, **kwargs):
        search = request.GET['search']
        movies = Movie.objects.filter(title__contains=search)
        seriess = Series.objects.filter(title__contains=search)
        actors_lname = Actor.objects.filter(last_name__contains=search) #Actor.objects.filter(first_name__contains=search)]
        actors_fname = Actor.objects.filter(first_name__contains=search) #Actor.objects.filter(first_name__contains=search)]
        directors_lname = Director.objects.filter(last_name__contains=search) #Director.objects.filter(first_name__contains=search)]
        directors_fname = Director.objects.filter(first_name__contains=search) #Director.objects.filter(first_name__contains=search)]
        searched = [movies, seriess, actors_lname, actors_fname, directors_lname, directors_fname]
        #print(movies, seriess, actors, directors)
        if searched:
            return render(request, 'catalog/search.html', {'searched':searched})    





