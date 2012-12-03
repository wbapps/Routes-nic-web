from app.models import Ruta, Trayectoria, Punto
from django.db.models import Q, Count

Punto.objects.filter(ruta__id=10).filter(ruta__id=59)
