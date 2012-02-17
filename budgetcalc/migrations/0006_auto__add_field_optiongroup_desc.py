# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Optiongroup.desc'
        db.add_column('budgetcalc_optiongroup', 'desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Optiongroup.desc'
        db.delete_column('budgetcalc_optiongroup', 'desc')


    models = {
        'budgetcalc.category': {
            'Meta': {'ordering': "['order']", 'object_name': 'Category'},
            'cat_type': ('django.db.models.fields.CharField', [], {'default': "'r'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'budgetcalc.option': {
            'Meta': {'ordering': "['order']", 'object_name': 'Option'},
            'amount': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['budgetcalc.Category']"}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'optiongroup': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['budgetcalc.Optiongroup']", 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'ridership': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'budgetcalc.optiongroup': {
            'Meta': {'object_name': 'Optiongroup'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'budgetcalc.submission': {
            'Meta': {'object_name': 'Submission'},
            'budget': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'selected_options'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['budgetcalc.Option']"})
        }
    }

    complete_apps = ['budgetcalc']
