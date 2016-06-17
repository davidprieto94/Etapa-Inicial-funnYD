from django.conf.urls import url
from django.contrib import admin
import actividades.views


urlpatterns = [
    url(r'^actividades/$', actividades.views.listActividades),
    url(r'^descripcionRD/$', actividades.views.descripcionRD),
]
