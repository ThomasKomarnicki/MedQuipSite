# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Order'
        db.create_table(u'Customers_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_skus', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('item_count', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('item_price', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('item_discount', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tax_total', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('shipping', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('shipped_to', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Customers', ['Order'])

        # Adding model 'Customer'
        db.create_table(u'Customers_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('orginization', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('orders', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('reset', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('reset_valid_through', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('user_cookie', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'Customers', ['Customer'])


    def backwards(self, orm):
        # Deleting model 'Order'
        db.delete_table(u'Customers_order')

        # Deleting model 'Customer'
        db.delete_table(u'Customers_customer')


    models = {
        u'Customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'first': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'orders': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'orginization': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'reset': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'reset_valid_through': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user_cookie': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'Customers.order': {
            'Meta': {'object_name': 'Order'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_count': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'item_discount': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'item_price': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'item_skus': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shipped_to': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shipping': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'tax_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        }
    }

    complete_apps = ['Customers']