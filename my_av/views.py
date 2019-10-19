import subprocess

from django.contrib.auth import authenticate, login, logout
from django.core.handlers.wsgi import WSGIRequest
from django.forms import modelformset_factory, Form
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView

from my_av.forms import ActressModelForm
from .models import Actress, Genre, Video


def index(request: WSGIRequest) -> HttpResponse:
    return redirect('my_av:movies')


def login_view(request: WSGIRequest) -> HttpResponse:
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return redirect('my_av:movies')


def logout_view(request: WSGIRequest) -> HttpResponse:
    logout(request)
    return redirect('my_av:index')


def movies(request):
    context = {
        'video_list': Video.objects.all(),
        'actress_list': Actress.objects.all(),
        'genre_list': Genre.objects.all(),
    }
    return render(request, 'my_av/movies.html', context)


def movie(request, video_id):
    video = Video.objects.get(pk=video_id)
    context = {
        'actress_list': video.actress.all(),
        'genre_list': video.genre.all(),
        'movie': video,
    }
    for a in context['actress_list']:
        a.a_slug = a.id
        a.g_slug = '-'
    return render(request, 'my_av/movie.html', context)


# TODO: clean genres part
def filter_view(request, actress_slug_ids: str, genre_slug_ids: str):
    video_qs = Video.objects

    if actress_slug_ids != '-':
        actress_id_list = actress_slug_ids.split('-')
        for actress_id in actress_id_list:
            video_qs = video_qs.filter(actress__id=actress_id)
        actress_slug_prefix = '{}-'.format('-'.join(actress_id_list))
    else:
        actress_slug_prefix = ''

    if genre_slug_ids != '-':
        genre_ids_list = genre_slug_ids.split('-')
        for genre_id in genre_ids_list:
            video_qs = video_qs.filter(genre__id=genre_id)
        genre_prefix_url = '{}-'.format('-'.join(genre_ids_list))
    else:
        genre_ids_list = []
        genre_prefix_url = ''

    video_ids = video_qs.values_list('id', flat=True)
    actress_list = Actress.objects.filter(video__in=video_ids).distinct()
    for a in actress_list:
        a.a_slug = actress_slug_prefix + str(a.id)
        a.g_slug = genre_slug_ids
    context = {
        'video_list': video_qs.distinct(),

        'actress_list': actress_list,
        'actress_slug_ids': actress_slug_ids,

        'genre_list': Genre.objects.filter(video__in=video_ids).distinct(),
        'genre_slug_ids': genre_slug_ids,
        'genre_ids_list': genre_ids_list,
        'genre_prefix_url': genre_prefix_url,
    }
    return render(request, 'my_av/filter.html', context)


# TODO: Change template and links of movies and movie.
def filter_soap(request):
    video_qs = Video.objects
    selected_actress_ids = request.GET.getlist('actress')
    selected_genre_ids = request.GET.getlist('genre')
    for actress_id in selected_actress_ids:
        video_qs = video_qs.filter(actress__id=actress_id)

    for genre_id in selected_genre_ids:
        video_qs = video_qs.filter(genre__id=genre_id)

    video_ids = video_qs.values_list('id', flat=True)
    actresses = Actress.objects.filter(video__in=video_ids).distinct()
    genres = Genre.objects.filter(video__in=video_ids).distinct()
    for actress in actresses:
        if str(actress.id) in selected_actress_ids:
            actress.selected = True

    for genre in genres:
        if str(genre.id) in selected_genre_ids:
            genre.selected = True

    ctx = {
        'video_list': video_qs.distinct(),
        'genres': genres,
        'actresses': actresses,
    }
    return render(request, 'my_av/filter-soap.html', ctx)


def filter_(request):
    pass


def temp(request: WSGIRequest) -> HttpResponse:
    print(request.get_full_path())
    # return redirect(request.get_full_path)
    # import threading
    # t = threading.Thread(target=play_movie)
    # t.start()
    return render(request, 'my_av/temp.html')


def play_movie(request: WSGIRequest) -> HttpResponse:
    subprocess.run(['vlc', 'http://mirror.cessen.com/blender.org/peach/trailer/trailer_iphone.m4v'])
    return redirect(request.get_full_path)


def my_test(request: WSGIRequest) -> HttpResponse:
    ActressFormSet = modelformset_factory(Actress, form=ActressModelForm)
    return render(request, 'test.html', {'formset': ActressFormSet})


class ActressList(ListView):
    queryset = Actress.objects.all().order_by('name')


class MovieList(ListView):
    queryset = Video.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'actress_list': ActressList.queryset,
        })
        return context


class FormSetView(FormView):
    form_class = modelformset_factory(Actress, form=ActressModelForm)
    template_name = 'my_av/form_set_view.html'
    success_url = '/my_av/form-set-view/'

    def form_valid(self, form: Form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        content = form.cleaned_data[0]['id']
        print(content.id)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        ids = request.GET.getlist('id')
        ActressFormset = modelformset_factory(Actress, form=ActressModelForm)
        formset = ActressFormset(queryset=Actress.objects.filter(id__in=ids))
        data = self.get_context_data(form=formset)
        return self.render_to_response(data)
