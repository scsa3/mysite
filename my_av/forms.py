from django import forms


class ActressForm(forms.Form):
    actress_id = forms.IntegerField(label='Actress ID')
    actress_name = forms.CharField(label='Actress Name')


class GenreForm(forms.Form):
    genre = forms.IntegerField(label='Genre ID')


class PathForm(forms.Form):
    source_folder_path = forms.CharField(max_length=123)
