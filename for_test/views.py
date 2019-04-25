from django.contrib.admin.views.main import ChangeList
from django.shortcuts import render
from django.db.models import Q, QuerySet
from django.http import HttpResponse
# from .models import Video, Actress, Genre
from .forms import UploadFileForm
from django.forms import formset_factory


def index(request):
    context1 = 'no'
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            # return HttpResponseRedirect('/success/url/')
            context1 = 'yes'
    else:
        form = UploadFileForm()
    return render(request, 'for_test/upload.html', {
        'form': form,
        'context1': context1,
    })
