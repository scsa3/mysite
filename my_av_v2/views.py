from django.forms import formset_factory
from django.shortcuts import render
from django.views.generic import FormView
from django_filters.views import FilterView

from my_av_v2.forms import ActressForm, MovieFormSet
from . import filters


def formset_test(request):
    ActressFormSet = formset_factory(
        ActressForm,
    )
    return render(request, 'test.html', {'formset': ActressFormSet})


class MovieFilterView(FilterView):
    filterset_class = filters.MovieFilter
    template_name = 'my_av_v2/movie_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MovieFormSetView(FormView):
    template_name = 'my_av_v2/movie_formset.html'
    form_class = MovieFormSet
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super().form_valid(form)
