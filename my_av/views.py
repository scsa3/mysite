from django.contrib.admin.views.main import ChangeList
from django.shortcuts import render
from django.db.models import Q, QuerySet
from django.http import HttpResponse
from .models import Video, Actress, Genre
from .forms import ActressForm, PathForm
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


def movie(request, video_id):
    video = Video.objects.get(pk=video_id)
    context = {
        'actress_list': video.actress.all(),
        'genre_list': video.genre.all(),
        'movie': video,
    }
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
    files = []
    if form.is_valid():
        path = form.cleaned_data['source_folder_path']
        path = Path(path)
        if path.is_dir() and path.exists():
            files = path.glob('**/*')
            print(files)
    else:
        form = PathForm()
    return render(request, 'my_av/file.html', {'form': form,
                                               'files': files})
