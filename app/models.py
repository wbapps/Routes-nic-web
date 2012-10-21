# -*- coding: utf-8 -*-
from django.db import models

class Ruta(models.Model):
	ruta		= models.CharField(max_length=60,unique=True)
	activo		= models.BooleanField(default=True)
	def __unicode__(self):		
		return self.ruta

class Punto(models.Model):   
	punto		= models.CharField(max_length=60,unique=True)
	lat			= models.DecimalField(max_digits=10, decimal_places=6)
	lon			= models.DecimalField(max_digits=10, decimal_places=6)
	def __unicode__(self):		
		return self.punto

class Trayectoria(models.Model):
	ruta_id		= models.ForeignKey(Ruta)
	punto_id	= models.ForeignKey(Punto)
	orden		= models.IntegerField()
	def __unicode__(self):		
		return str(self.ruta_id)

class Recorrido(models.Model):
	ruta		= models.ForeignKey(Ruta)
	lat			= models.DecimalField(max_digits=10, decimal_places=6)
	lon			= models.DecimalField(max_digits=10, decimal_places=6)
	orden		= models.IntegerField()