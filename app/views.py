# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Ruta, Trayectoria, Punto

def rutas_view(request):
	rutas = Ruta.objects.all()
	ctx = {'rutas':rutas}
	return render_to_response('rutas.html',ctx,context_instance=RequestContext(request))

def puntos_view(request):
	puntos = Trayectoria.objects.filter(ruta_id=6)
	ctx = {'puntos':puntos}
	return render_to_response('puntos.html',ctx,context_instance=RequestContext(request))