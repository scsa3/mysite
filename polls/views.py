from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Video


def index(request):
    # video_list = Video.objects.iterator()
    # context = {'video_list': video_list}
    # return render(request, 'polls/login.html', context)
    return HttpResponse("Hello, world. You're at the my_av index.")


def detail(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'video': video})
    # return HttpResponse("You're looking at question %s." % video_id)
