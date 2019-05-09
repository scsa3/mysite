from django.urls import path

from . import views

app_name = 'my_av'
urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('search/', views.search, name='search'),
    path('movie/<int:video_id>/', views.movie, name='movie'),
    path('file/', views.parse_folder, name='file'),
    path('tool/', views.input_path, name='input'),
    path('tool/movie', views.list_movie, name='tool-list-movie'),

    # TODO:Using in pages
    path('movies/filter-by/actress/<str:actress_slug_ids>/genre/<str:genre_slug_ids>/', views.filter_, name='filter'),
]
