from django.urls import path

from . import views

app_name = 'tools'
urlpatterns = [
    path('tools/', views.tool, name='tools'),
    path('tools/movie', views.list_movie, name='tools-list-movie'),
    path('tools/list-nfos/', views.list_nfos, name='tools-list-nfos'),
    path('tools/import-nfos/', views.import_nfos, name='import-nfos'),
]
