# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CecaResponse'
        db.create_table(u'shop_ceca_cecaresponse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant_id', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('acquirer_bin', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('terminal_id', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('num_operacion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('importe', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('tipo_moneda', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('referencia', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('firma', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('numero_autorizacion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('idioma', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('shop_ceca', ['CecaResponse'])


    def backwards(self, orm):
        # Deleting model 'CecaResponse'
        db.delete_table(u'shop_ceca_cecaresponse')


    models = {
        'shop_ceca.cecaresponse': {
            'Meta': {'object_name': 'CecaResponse'},
            'acquirer_bin': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'firma': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'importe': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'merchant_id': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'num_operacion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'numero_autorizacion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'referencia': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'terminal_id': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'tipo_moneda': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['shop_ceca']