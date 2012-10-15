# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Ruta

def rutas_view(request):
	rutas = Ruta.objects.all()
	ctx = {'rutas':rutas}
	return render_to_response('rutas.html',ctx,context_instance=RequestContext(request))