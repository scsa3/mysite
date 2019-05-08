from django.urls import path

from . import views

app_name = 'my_av'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('movie/<int:video_id>/', views.movie, name='movie'),
    path('file/', views.parse_folder, name='file'),
    path('tool/', views.input_path, name='input'),
    path('tool/movie', views.list_movie, name='tool-list-movie'),

    # TODO:Using in pages
    path('movies/filter-by/actress/<slug:actress_slug_ids>/genre/<slug:genre_slug_ids>', views.movie_filter),
]
