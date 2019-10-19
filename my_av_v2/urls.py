from django.urls import path

from . import views

app_name = 'my_av_v2'
urlpatterns = [
    path('', views.MovieFilterView.as_view()),
    path('formset/', views.MovieFormSetView.as_view()),
]
