from django.contrib.auth import authenticate, login, logout

from django.contrib.admin.views.main import ChangeList
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.db.models import Q, QuerySet
from django.http import HttpResponse
from django.urls import reverse

from .forms import GenreFormSet

from my_av.tools import nfo_importer, videos_finder, nfos_finder
from .models import Video, Actress, Genre
from .forms import ActressForm, PathForm, PathFormSet
from django.forms import formset_factory
from pathlib import Path


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
        'genres': genres,
        'actresses': actresses,
    }
    return render(request, 'my_av/filter-soap.html', ctx)


def temp(request: WSGIRequest) -> HttpResponse:
    return render(request, 'my_av/temp.html')


# TODO: All of tool part
def tool(request):
    return render(request, 'my_av/tool/tool.html', {'form': PathForm()})


def parse_folder(request):
    form = PathForm(request.GET)

    if form.is_valid():
        source_folder_path_str = form.cleaned_data['path']
        source_folder_path = Path(source_folder_path_str)
        nfos_path = nfos_finder(source_folder_path)
        [nfo_importer(path) for path in nfos_path]

    else:
        nfos_path = []
        form = PathForm()
    return render(request, 'my_av/file.html', {'form': form,
                                               'nfos_path': nfos_path})


def list_movie(request):
    form = PathForm(request.GET)
    if form.is_valid():
        path_str = form.cleaned_data['path']
        path = Path(path_str)
        movie_paths = videos_finder(path)
        return render(request, 'my_av/tool/list-paths.html', {'paths': movie_paths})
    else:
        context = {'error': form.errors, 'form': PathForm()}
        return render(request, 'my_av/tool/tool.html', context)


def list_files(request, source_path: str):
    if source_path:
        path = Path(source_path)
        movie_paths = videos_finder(path)
        context = {'paths': movie_paths}
    else:
        context = dict()
    return request(request, 'my_av/tool/list-files.html', context)


def list_nfos(request: WSGIRequest) -> HttpResponse:
    source_path = request.GET['source-path']
    path = Path(source_path)
    paths = nfos_finder(path)
    return render(request, 'my_av/tool/list-nfos.html', {'source_path': source_path, 'paths': paths})


def import_nfos(request: WSGIRequest) -> HttpResponse:
    source_path = request.GET['source-path']
    path = Path(source_path)
    paths = nfos_finder(path)
    for nfo in paths:
        nfo_importer(nfo)

    return redirect(to=reverse('admin:index'))
