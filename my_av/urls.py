from django.urls import path

import tools.views
from . import views

app_name = 'my_av'
urlpatterns = [
    path('', views.login_view, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('movies/', views.movies, name='movies'),
    path('movie/<int:video_id>/', views.movie, name='movie'),
    path('file/', tools.views.parse_folder, name='file'),
    path('tools/', tools.views.tool, name='tools'),
    path('tools/movie', tools.views.list_movie, name='tools-list-movie'),
    path('tools/list-nfos/', tools.views.list_nfos, name='tools-list-nfos'),
    path('tools/import-nfos/', tools.views.import_nfos, name='import-nfos'),
    # path('tools/path/<str:source_path>/files/', views.list_files, name='tools-list-files'),
    path('movies/filter-by/actress/<str:actress_slug_ids>/genre/<str:genre_slug_ids>/', views.filter_view, name='filter'),
    path('movies/filter-by/', views.filter_soap, name='filter-soap'),
    path('temp/', views.temp, name='temp')
]
