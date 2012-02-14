# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Submission'
        db.create_table('budgetcalc_submission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('budgetcalc', ['Submission'])

        # Adding M2M table for field options on 'Submission'
        db.create_table('budgetcalc_submission_options', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('submission', models.ForeignKey(orm['budgetcalc.submission'], null=False)),
            ('option', models.ForeignKey(orm['budgetcalc.option'], null=False))
        ))
        db.create_unique('budgetcalc_submission_options', ['submission_id', 'option_id'])


    def backwards(self, orm):
        
        # Deleting model 'Submission'
        db.delete_table('budgetcalc_submission')

        # Removing M2M table for field options on 'Submission'
        db.delete_table('budgetcalc_submission_options')


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
            'optiongroup': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['budgetcalc.Optiongroup']", 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'budgetcalc.optiongroup': {
            'Meta': {'object_name': 'Optiongroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'budgetcalc.submission': {
            'Meta': {'object_name': 'Submission'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'selected_options'", 'symmetrical': 'False', 'to': "orm['budgetcalc.Option']"})
        }
    }

    complete_apps = ['budgetcalc']
