# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field ruta on 'Punto'
        db.create_table('app_punto_ruta', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('punto', models.ForeignKey(orm['app.punto'], null=False)),
            ('ruta', models.ForeignKey(orm['app.ruta'], null=False))
        ))
        db.create_unique('app_punto_ruta', ['punto_id', 'ruta_id'])


    def backwards(self, orm):
        # Removing M2M table for field ruta on 'Punto'
        db.delete_table('app_punto_ruta')


    models = {
        'app.punto': {
            'Meta': {'object_name': 'Punto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'punto': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'ruta': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'puntos'", 'symmetrical': 'False', 'to': "orm['app.Ruta']"})
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
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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