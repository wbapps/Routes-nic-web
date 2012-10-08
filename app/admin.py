#encoding:utf-8 
from django.contrib import admin
from app.models import Ruta, Punto, Trayectoria, Recorrido

class RutaInline(admin.TabularInline):
	model = Trayectoria
	extra = 1

class RutaAdmin(admin.ModelAdmin):
	ordering =  ['id']
	inlines = [RutaInline]
	
class PuntoAdmin(admin.ModelAdmin):
	list_display	= ['punto','lat','lon']
	search_fields	= ['punto',]
	ordering =  ['punto']

class TrayectoriaAdmin(admin.ModelAdmin):
	list_display	= ['ruta_id','punto_id','orden']
	search_fields	= ['ruta_id__ruta','punto_id__punto']
	list_filter		= ['ruta_id',]
	
class RecorridoAdmin(admin.ModelAdmin):
	list_display	= ['ruta','lat','lon','orden']	
	

admin.site.register(Ruta, RutaAdmin)
admin.site.register(Punto, PuntoAdmin)
admin.site.register(Trayectoria, TrayectoriaAdmin)
admin.site.register(Recorrido, RecorridoAdmin)