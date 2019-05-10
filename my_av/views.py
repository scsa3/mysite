from django.contrib.admin.views.main import ChangeList
from django.shortcuts import render
from django.db.models import Q, QuerySet
from django.http import HttpResponse

from my_av.tools import nfo_importer, videos_finder, nfos_finder
from .models import Video, Actress, Genre
from .forms import ActressForm, PathForm, PathFormSet
from django.forms import formset_factory
from pathlib import Path


def index(request):
    actress_form_set = formset_factory(ActressForm)
    form_set = actress_form_set(initial=[
        {'actress_id': 1, 'actress_name': 'name1'},
        {'actress_id': 1, 'actress_name': 'name1'},
    ])
    context = {
        'video_list': Video.objects.all(),
        'actress_list': Actress.objects.all(),
        'genre_list': Genre.objects.all(),
        'form_set': form_set
    }
    return render(request, 'my_av/index.html', context)


def movies(request):
    context = {
        'video_list': Video.objects.all(),
        'actress_list': Actress.objects.all(),
        'genre_list': Genre.objects.all(),
    }
    return render(request, 'my_av/index.html', context)


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


def search(request):
    # TODO: Need replace by forms.py
    video_qs = Video.objects
    actress_ids = request.GET.getlist('actress', [])
    for actress_id in actress_ids:
        video_qs = video_qs.filter(actress__id=actress_id)

    genre_ids = request.GET.getlist('genre', [])
    for genre_id in genre_ids:
        video_qs = video_qs.filter(genre__id=genre_id)

    video_ids = video_qs.values_list('id', flat=True)
    context = {
        'video_list': video_qs.distinct(),
        'actress_list': Actress.objects.filter(video__in=video_ids).distinct(),
        'genre_list': Genre.objects.filter(video__in=video_ids).distinct(),
    }
    return render(request, 'my_av/search.html', context)


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
        return render(request, 'my_av/tool/path-list.html', {'paths': movie_paths})
    else:
        context = {'error': form.errors, 'form': PathForm()}
        return render(request, 'my_av/tool/input-path.html', context)


def input_path(request):
    return render(request, 'my_av/tool/input-path.html', {'form': PathForm()})


# TODO:change details
def filter_(request, actress_slug_ids: str, genre_slug_ids: str):
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


def temp(request):
    return render(request, 'my_av/temp.html')
