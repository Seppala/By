# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'CustomUser.is_upfo'
        db.add_column('upfoMain_customuser', 'is_upfo', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'CustomUser.is_upfo'
        db.delete_column('upfoMain_customuser', 'is_upfo')


    models = {
        'upfoMain.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_upfo': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['upfoMain']
