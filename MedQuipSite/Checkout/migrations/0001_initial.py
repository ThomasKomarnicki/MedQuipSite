# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Checkout'
        db.create_table(u'Checkout_checkout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('payment_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('shipping_cost', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2, blank=True)),
            ('shipping_method', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'Checkout', ['Checkout'])

        # Adding model 'Address'
        db.create_table(u'Checkout_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Customers.Customer'])),
            ('checkout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Checkout.Checkout'])),
            ('first', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('orginization', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'Checkout', ['Address'])

        # Adding model 'CreditCard'
        db.create_table(u'Checkout_creditcard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('checkout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Checkout.Checkout'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('exp_date', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cvc', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Checkout', ['CreditCard'])


    def backwards(self, orm):
        # Deleting model 'Checkout'
        db.delete_table(u'Checkout_checkout')

        # Deleting model 'Address'
        db.delete_table(u'Checkout_address')

        # Deleting model 'CreditCard'
        db.delete_table(u'Checkout_creditcard')


    models = {
        u'Checkout.address': {
            'Meta': {'object_name': 'Address'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'checkout': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Checkout.Checkout']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Customers.Customer']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'first': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'orginization': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Checkout.checkout': {
            'Meta': {'object_name': 'Checkout'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shipping_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'shipping_method': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'Checkout.creditcard': {
            'Meta': {'object_name': 'CreditCard'},
            'checkout': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Checkout.Checkout']"}),
            'cvc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'exp_date': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
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
        }
    }

    complete_apps = ['Checkout']