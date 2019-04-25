from django import forms


class UploadFileForm(forms.Form):
    path = forms.CharField()
