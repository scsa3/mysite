from pathlib import Path

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from my_av.forms import PathForm
from .utilities import nfos_finder, import_nfo, videos_finder
from tools import utilities


def index(request):
    return render(request, 'tools/index.html', {'form': PathForm()})


def import_movie(request: WSGIRequest) -> HttpResponse:
    if request.GET:
        path_str = request.GET['path']
        path = Path(path_str)
        utilities.create_nfo(path)
        nfo_path = Path(path_str[:-3] + 'nfo')
        if nfo_path.exists():
            import_nfo(nfo_path)
            context = {'message': 'Done {}'.format(path_str)}
        else:
            context = {'message': 'Fail {}'.format(path_str)}
    else:
        context = {'message': ''}
    return render(request, 'tools/create-nfo.html', context)


def list_nfos(request: WSGIRequest) -> HttpResponse:
    source_path = request.GET['source-path']
    path = Path(source_path)
    paths = nfos_finder(path)
    return render(request, 'tools/list-nfos.html', {'source_path': source_path, 'paths': paths})


def parse_folder(request):
    form = PathForm(request.GET)

    if form.is_valid():
        source_folder_path_str = form.cleaned_data['path']
        source_folder_path = Path(source_folder_path_str)
        nfos_path = nfos_finder(source_folder_path)
        [import_nfo(path) for path in nfos_path]

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
        return render(request, 'tools/list-paths.html', {'paths': movie_paths})
    else:
        context = {'error': form.errors, 'form': PathForm()}
        return render(request, 'tools/index.html', context)


def list_files(request, source_path: str):
    if source_path:
        path = Path(source_path)
        movie_paths = videos_finder(path)
        context = {'paths': movie_paths}
    else:
        context = dict()
    return render(request, 'my_av/tools/list-files.html', context)


def import_nfos(request: WSGIRequest) -> HttpResponse:
    source_path = request.GET['source-path']
    path = Path(source_path)
    paths = nfos_finder(path)
    for nfo in paths:
        import_nfo(nfo)

    return redirect(to=reverse('admin:index'))
