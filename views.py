from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from .forms import BaseForm
from .models import Person


def index(request):

    return render(request, 'index.html')
    # show_data = Person.objects.all()
    #
    # return render(request, 'index.html', {'show_data': show_data})


def create_person(request):

    form = BaseForm()

    if form.is_valid():
        person = Person(**form.cleaned_data)
        person.save()

    return render(request, 'create.html', {'form': form})


def change_person(request, p_id):

    if request.POST:
        form = BaseForm(request.POST)
        per = request.POST.get('name', '')
        date = request.POST.get('birth_date', '')
        person, created = Person.objects.update_or_create(pk=p_id, defaults={'name': per, 'birth_date': date})

        if form.is_valid():
            form.save()

    person = Person.objects.filter(pk=p_id).first()
    form = BaseForm(instance=person)

    return render(request, 'name.html', {'form': form})
