from django import forms
# from tutor.widgets import DateInput
from tutor.models import Person, PersonData
from tutorial import settings
from django.db import models


class BaseForm(forms.ModelForm):
    class Meta:
        model = Person
        labels = {'name': 'Имя Сотрудника', 'birth_date': 'Дата Рождения'}
        widgets = {'birth_date': forms.DateInput(attrs={'class': 'datepicker'})}
        exclude = ()
