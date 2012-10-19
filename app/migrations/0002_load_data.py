# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        from django.core.management import call_command
		call_command("loaddata", "initial_data.json")

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'app.punto': {
            'Meta': {'object_name': 'Punto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'punto': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        'app.recorrido': {
            'Meta': {'object_name': 'Recorrido'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'orden': ('django.db.models.fields.IntegerField', [], {}),
            'ruta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Ruta']"})
        },
        'app.ruta': {
            'Meta': {'object_name': 'Ruta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ruta': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        'app.trayectoria': {
            'Meta': {'object_name': 'Trayectoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.IntegerField', [], {}),
            'punto_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Punto']"}),
            'ruta_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Ruta']"})
        }
    }

    complete_apps = ['app']
    symmetrical = True
