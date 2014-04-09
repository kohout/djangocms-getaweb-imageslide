# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageSlider'
        db.create_table(u'djangocms_imageslider_imageslider', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'djangocms_imageslider', ['ImageSlider'])

        # Adding model 'ImageSliderItem'
        db.create_table(u'djangocms_imageslider_imageslideritem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djangocms_imageslider.ImageSlider'])),
            ('ordering', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True)),
            ('image_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
        ))
        db.send_create_signal(u'djangocms_imageslider', ['ImageSliderItem'])


    def backwards(self, orm):
        # Deleting model 'ImageSlider'
        db.delete_table(u'djangocms_imageslider_imageslider')

        # Deleting model 'ImageSliderItem'
        db.delete_table(u'djangocms_imageslider_imageslideritem')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'djangocms_imageslider.imageslider': {
            'Meta': {'object_name': 'ImageSlider', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'djangocms_imageslider.imageslideritem': {
            'Meta': {'object_name': 'ImageSliderItem'},
            'alt': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True'}),
            'image_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True'}),
            'ordering': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'slider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangocms_imageslider.ImageSlider']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'})
        }
    }

    complete_apps = ['djangocms_imageslider']