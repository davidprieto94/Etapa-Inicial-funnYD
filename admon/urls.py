from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admon/ingresar/$', 'admon.views.ingresar', name='admon_ingresar'),
]
