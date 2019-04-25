from django.urls import path

from . import views

app_name = 'for_test'
urlpatterns = [
    path('', views.index, name='index'),
]
