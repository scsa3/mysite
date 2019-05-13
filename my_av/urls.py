from django.urls import path

from . import views

app_name = 'my_av'
urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('movie/<int:video_id>/', views.movie, name='movie'),
    path('file/', views.parse_folder, name='file'),
    path('tool/', views.tool, name='tool'),
    path('tool/movie', views.list_movie, name='tool-list-movie'),
    path('tool/movie/list-nfos/', views.list_nfos, name='tool-list-nfos'),
    path('tool/movie/import-nfos/', views.import_nfos, name='import-nfos'),
    # path('tool/path/<str:source_path>/files/', views.list_files, name='tool-list-files'),
    path('movies/filter-by/actress/<str:actress_slug_ids>/genre/<str:genre_slug_ids>/', views.filter_, name='filter'),
    path('movies/filter-by/', views.filter_soap, name='filter-soap'),
    path('temp/', views.temp, name='temp')
]
