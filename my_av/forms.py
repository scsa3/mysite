from django import forms
from django.forms import formset_factory


class ActressForm(forms.Form):
    actress_id = forms.IntegerField(label='Actress ID')
    actress_name = forms.CharField(label='Actress Name')


class GenreForm(forms.Form):
    genre = forms.IntegerField(label='Genre ID')


class PathForm(forms.Form):
    path = forms.CharField(max_length=123)


PathFormSet = formset_factory(PathForm)
