from django.forms import ModelForm, modelformset_factory
from .models import Actress, Genre


class ActressForm(ModelForm):
    class Meta:
        model = Actress
        fields = '__all__'


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


GenreFormSet = modelformset_factory(Genre, form=GenreForm)
