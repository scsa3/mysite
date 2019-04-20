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
    actress_ids = request.GET.get('actress', [])
    # actress_qs = Video.objects.filter(actress__in=actress_ids)
    actress_qs = Video.objects.all()
    for actress_id in actress_ids:
        print(actress_id)
        actress_qs = actress_qs.filter(actress=actress_id)

    genre_list = request.GET.get('genre', [])
    genre_qs = Video.objects.filter(genre__in=genre_list)
    video_list = (actress_qs| genre_qs).distinct()
    video_ids = video_list.values_list('id', flat=True).distinct()

    context = {
        'video_list': Video.objects.filter(id__in=video_ids),
        'actress_list': Actress.objects.filter(video__in=video_ids).distinct(),
        'genre_list': Genre.objects.filter(video__in=video_ids).distinct(),
    }
    return render(request, 'my_av/search.html', context)
