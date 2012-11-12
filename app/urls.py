# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('app.views',	
    url(r'^admin/', include(admin.site.urls)), 
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^$','rutas_view', name='rutas_view'),
    url(r'^puntos/$','puntos_view', name='puntos_view'),
    url(r'^buscar/$','buscar_view', name='buscar_view'),
)
