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
    result = "#result_%s" % id_ruta
    dajax.assign(result,'innerHTML', ''.join(out))
    return dajax.json()