from django.conf.urls import url
from django.contrib import admin

from admon.views import loginAdmonView, dashBoardView

urlpatterns = [
		url(r'^admon/$', dashBoardView.as_view(), name='dash_board'),
		url(r'^admon/ingresar/$', loginAdmonView.as_view(), name='admon_ingresar'),
]
