from django.shortcuts import render
from django.db.models import Q, QuerySet
from django.http import HttpResponse
from .models import Video, Actress, Genre


def index(request):
    context = {
        'video_list': Video.objects.all(),
        'actress_list': Actress.objects.all(),
        'genre_list': Genre.objects.all(),
    }
    return render(request, 'my_av/index.html', context)


def detail(request, video_id):
    video = Video.objects.get(pk=video_id)
    context = {
        'title': video.title,
        'fanart_url': video.fanart_url,
        'actress': video.actress.all(),
        'genre': video.genre.all()
    }
    return render(request, 'my_av/detail.html', context)


def search(request):
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
