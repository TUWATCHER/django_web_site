from django.db import models
import datetime


class Person(models.Model):
    name = models.CharField(max_length=110)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class PersonData(models.Model):
    worker = models.ForeignKey(Person)
    job_title = models.CharField(max_length=20)
    payment = models.IntegerField()
    currently_emp = models.BooleanField()

    def __str__(self):
        return '{0}, {1}'.format(self.worker, self.payment)
