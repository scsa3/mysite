from django import forms
from django.forms import formset_factory, modelformset_factory

from .models import Genre, Actress


class ActressForm(forms.Form):
    actress_id = forms.IntegerField(label='Actress ID')
    actress_name = forms.CharField(label='Actress Name')


class GenreForm(forms.Form):
    id = forms.IntegerField(label='Genre ID')


class PathForm(forms.Form):
    attrs = {'style': 'width: 100%'}
    widget = forms.TextInput(attrs=attrs)
    path = forms.CharField(max_length=255, widget=widget)


PathFormSet = formset_factory(PathForm)
GenreFormSet = modelformset_factory(Genre, fields=['id'])


class ActressModelForm(forms.ModelForm):
    class Meta:
        model = Actress
        fields = '__all__'
