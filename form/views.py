from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from create.models import testdata
from create.views import create
from delete.views import delete
from form.form import google_Form
from form.serializer import UserSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render

from update.views import update


def google_Form_choice(choice):
    if choice=="create":
        return create()
    elif choice=="delete":
        return delete()
    else:return update()
def form_templates(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = google_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = google_Form()

    return render(request, 'form.html', {'form': form})

#serializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = testdata.objects.all()
    serializer_class= UserSerializer


