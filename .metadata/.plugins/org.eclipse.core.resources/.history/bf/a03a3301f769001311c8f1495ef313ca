# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'Products_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('children_ids', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('parent_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'Products', ['Category'])

        # Adding model 'Product'
        db.create_table(u'Products_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('img', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('category_id', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute_type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Products', ['Product'])

        # Adding model 'Attribute'
        db.create_table(u'Products_attribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Products.Product'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Products', ['Attribute'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'Products_category')

        # Deleting model 'Product'
        db.delete_table(u'Products_product')

        # Deleting model 'Attribute'
        db.delete_table(u'Products_attribute')


    models = {
        u'Products.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Products.Product']"}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'Products.category': {
            'Meta': {'object_name': 'Category'},
            'children_ids': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'Products.product': {
            'Meta': {'object_name': 'Product'},
            'attribute_type': ('django.db.models.fields.IntegerField', [], {}),
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['Products']