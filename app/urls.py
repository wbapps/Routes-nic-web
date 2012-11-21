# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('app.views',
	url(r'^$','rutas_view', name='rutas_view'),
	url(r'^puntos/$','puntos_view', name='puntos_view'),
    url(r'^buscar/$','buscar_view', name='buscar_view'),
)