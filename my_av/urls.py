from django.urls import path

from . import views

app_name = 'my_av'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('movie/<int:video_id>/', views.movie, name='movie'),
    path('file/', views.parse_folder, name='file'),
]
