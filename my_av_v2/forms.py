from django.forms import ModelForm, modelformset_factory

from my_av.models import Actress, Genre
from . import models


class ActressForm(ModelForm):
    class Meta:
        model = Actress
        fields = '__all__'


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


MovieFormSet = modelformset_factory(models.Video, fields=('id', 'title'))
