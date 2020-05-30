from django.conf.urls import url,include
from django.shortcuts import render
from django.http import HttpResponse
from Apps.adopcion.views import index_adopcion
urlpatterns = [
    url(r'^$', index_adopcion),
]