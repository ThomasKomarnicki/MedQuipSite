# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Attribute.price_currency'
        db.add_column(u'Products_attribute', 'price_currency',
                      self.gf('djmoney.models.fields.CurrencyField')(default='USD'),
                      keep_default=False)


        # Changing field 'Attribute.price'
        db.alter_column(u'Products_attribute', 'price', self.gf('djmoney.models.fields.MoneyField')(max_digits=10, decimal_places=2, default_currency='USD'))
        # Adding field 'Product.price_currency'
        db.add_column(u'Products_product', 'price_currency',
                      self.gf('djmoney.models.fields.CurrencyField')(default='USD'),
                      keep_default=False)


        # Changing field 'Product.price'
        db.alter_column(u'Products_product', 'price', self.gf('djmoney.models.fields.MoneyField')(max_digits=10, decimal_places=2, default_currency='USD'))

    def backwards(self, orm):
        # Deleting field 'Attribute.price_currency'
        db.delete_column(u'Products_attribute', 'price_currency')


        # Changing field 'Attribute.price'
        db.alter_column(u'Products_attribute', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2))
        # Deleting field 'Product.price_currency'
        db.delete_column(u'Products_product', 'price_currency')


        # Changing field 'Product.price'
        db.alter_column(u'Products_product', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2))

    models = {
        u'Products.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('djmoney.models.fields.MoneyField', [], {'max_digits': '10', 'decimal_places': '2', 'default_currency': "'USD'"}),
            'price_currency': ('djmoney.models.fields.CurrencyField', [], {'default': "'USD'"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Products.Product']"}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'Products.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'Products.product': {
            'Meta': {'object_name': 'Product'},
            'attribute_options': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'attribute_type': ('django.db.models.fields.IntegerField', [], {}),
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.CharField', [], {'default': "'0.jpg'", 'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('djmoney.models.fields.MoneyField', [], {'max_digits': '10', 'decimal_places': '2', 'default_currency': "'USD'"}),
            'price_currency': ('djmoney.models.fields.CurrencyField', [], {'default': "'USD'"}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '5', 'blank': 'True'})
        }
    }

    complete_apps = ['Products']