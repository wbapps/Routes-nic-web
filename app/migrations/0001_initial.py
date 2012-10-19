# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ruta'
        db.create_table('app_ruta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruta', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal('app', ['Ruta'])

        # Adding model 'Punto'
        db.create_table('app_punto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('punto', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('lon', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
        ))
        db.send_create_signal('app', ['Punto'])

        # Adding model 'Trayectoria'
        db.create_table('app_trayectoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruta_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Ruta'])),
            ('punto_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Punto'])),
            ('orden', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('app', ['Trayectoria'])

        # Adding model 'Recorrido'
        db.create_table('app_recorrido', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ruta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Ruta'])),
            ('lat', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('lon', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('orden', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('app', ['Recorrido'])


    def backwards(self, orm):
        # Deleting model 'Ruta'
        db.delete_table('app_ruta')

        # Deleting model 'Punto'
        db.delete_table('app_punto')

        # Deleting model 'Trayectoria'
        db.delete_table('app_trayectoria')

        # Deleting model 'Recorrido'
        db.delete_table('app_recorrido')


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