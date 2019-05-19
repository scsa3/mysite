from django.urls import path

from . import views

app_name = 'tools'
urlpatterns = [
    path('', views.index, name='index'),
    path('import-movie/', views.import_movie, name='import-movie'),
    path('movie/', views.list_movie, name='tools-list-movie'),
    path('list-nfos/', views.list_nfos, name='tools-list-nfos'),
    path('import-nfos/', views.import_nfos, name='import-nfos'),
]
