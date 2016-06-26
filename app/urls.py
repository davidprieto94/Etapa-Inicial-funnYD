from django.conf.urls import url
from django.contrib import admin

import app.views

urlpatterns = [
    url(r'^$', app.views.inicio),
     url(r'^registro/$', app.views.registro),
]
