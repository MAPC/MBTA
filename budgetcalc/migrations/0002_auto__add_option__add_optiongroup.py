# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Option'
        db.create_table('budgetcalc_option', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('amount', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['budgetcalc.Category'])),
            ('optiongroup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budgetcalc.Optiongroup'], null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('budgetcalc', ['Option'])

        # Adding model 'Optiongroup'
        db.create_table('budgetcalc_optiongroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('budgetcalc', ['Optiongroup'])


    def backwards(self, orm):
        
        # Deleting model 'Option'
        db.delete_table('budgetcalc_option')

        # Deleting model 'Optiongroup'
        db.delete_table('budgetcalc_optiongroup')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'optiongroup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['budgetcalc.Optiongroup']", 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'budgetcalc.optiongroup': {
            'Meta': {'object_name': 'Optiongroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['budgetcalc']
