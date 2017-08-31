# from django import forms
# from django.utils.safestring import mark_safe
#
# class DateInput(forms.DateInput):
#     def __init__(self, *args, **kwargs):
#         print('label3')
#         super(DateInput, self).__init__(*args, **kwargs)
#        #print('label4')
#     def render(self, name, value):
#         print(value)
#         return mark_safe("<input type='date' value ='{0}'".format(str(value)))