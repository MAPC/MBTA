# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('budgetcalc_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cat_type', self.gf('django.db.models.fields.CharField')(default='r', max_length=1)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('budgetcalc', ['Category'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('budgetcalc_category')


    models = {
        'budgetcalc.category': {
            'Meta': {'ordering': "['order']", 'object_name': 'Category'},
            'cat_type': ('django.db.models.fields.CharField', [], {'default': "'r'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['budgetcalc']
