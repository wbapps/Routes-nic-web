# -*- coding: utf-8 -*-
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from models import Ruta, Punto, Trayectoria, Recorrido

@dajaxice_register
def puntosInteres(request, id_ruta):
    dajax 	= Dajax()
    puntos 	= Trayectoria.objects.filter(ruta_id=id_ruta)
    out		= []    
    for punto in puntos:
    	out.append("<li>%s</li>" % punto.punto_id.punto)
    dajax.assign("#puntosInteres",'innerHTML', out)
    return dajax.json()

@dajaxice_register
def nombreRuta(request, id_ruta):
    dajax 	= Dajax()
    nombre 	= Ruta.objects.get(id=id_ruta) 
    out     = []    
    out.append("%s" % nombre)
    dajax.assign("#nombreRuta",'innerHTML', out)
    return dajax.json()