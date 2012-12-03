# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import buscarRutasForm
from models import Ruta, Trayectoria, Punto
from django.db.models import Count

def rutas_view(request):
	rutas = Ruta.objects.filter(activo=True)
	ctx = {'rutas':rutas}
	return render_to_response('rutas.html',ctx,context_instance=RequestContext(request))

def puntos_view(request):
	puntos = Trayectoria.objects.all()
	ctx = {'puntos':puntos}
	return render_to_response('puntos.html',ctx,context_instance=RequestContext(request))

def buscar_view(request):
    #request.POST.getlist('puntos')

    #BUSCAR n RUTAS
    '''def obtener_puntos(model_class, m2m_field, ids):
        query = model_class.objects.annotate(count=Count(m2m_field)).filter(count=len(ids))
        for _id in ids:
            query = query.filter(id=_id)
            return query
    info = obtener_puntos(Punto, 'ruta', query)'''
    #info =Punto.objects.annotate(count=Count('ruta')).filter(id=10).filter(id=59).filter(count=2)
    info = Punto.objects.filter(ruta__id=10).filter(ruta__id=59)
    
        #else:
            #info = ["informacion con datos incorrectos",]		
    form = buscarRutasForm()
    ctx = {'form':form, 'info':info}
    return render_to_response('buscar.html',ctx,context_instance=RequestContext(request))