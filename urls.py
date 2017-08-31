from django.conf.urls import url
from django.contrib import admin
from tutor import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index$', views.index, name='index'),
    url(r'^create$', views.create_person, name='create'),
    url(r'^(?P<p_id>[0-9]+)$', views.change_person, name='tutor')
]
