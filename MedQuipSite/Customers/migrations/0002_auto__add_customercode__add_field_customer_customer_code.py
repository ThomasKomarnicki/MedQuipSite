# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomerCode'
        db.create_table(u'Customers_customercode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price_discount_percent', self.gf('django.db.models.fields.IntegerField')()),
            ('free_shipping', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('shipping_discount_precent', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Customers', ['CustomerCode'])

        # Adding field 'Customer.customer_code'
        db.add_column(u'Customers_customer', 'customer_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'CustomerCode'
        db.delete_table(u'Customers_customercode')

        # Deleting field 'Customer.customer_code'
        db.delete_column(u'Customers_customer', 'customer_code')


    models = {
        u'Customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'customer_code': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
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
        u'Customers.customercode': {
            'Meta': {'object_name': 'CustomerCode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'free_shipping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_discount_percent': ('django.db.models.fields.IntegerField', [], {}),
            'shipping_discount_precent': ('django.db.models.fields.IntegerField', [], {})
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