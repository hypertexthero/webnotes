# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Notes.added_at'
        db.delete_column('notes_notes', 'added_at')

        # Deleting field 'Notes.last_update'
        db.delete_column('notes_notes', 'last_update')

        # Deleting field 'Notes.content'
        db.delete_column('notes_notes', 'content')

        # Adding field 'Notes.content_markdown'
        db.add_column('notes_notes', 'content_markdown', self.gf('django.db.models.fields.TextField')(default=datetime.date(2012, 1, 9)), keep_default=False)

        # Adding field 'Notes.content_html'
        db.add_column('notes_notes', 'content_html', self.gf('django.db.models.fields.TextField')(default=datetime.date(2012, 1, 9)), keep_default=False)

        # Adding field 'Notes.created'
        db.add_column('notes_notes', 'created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now), keep_default=False)

        # Adding field 'Notes.modified'
        db.add_column('notes_notes', 'modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Notes.added_at'
        db.add_column('notes_notes', 'added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2012, 1, 9), blank=True), keep_default=False)

        # Adding field 'Notes.last_update'
        db.add_column('notes_notes', 'last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2012, 1, 9), blank=True), keep_default=False)

        # Adding field 'Notes.content'
        db.add_column('notes_notes', 'content', self.gf('django.db.models.fields.TextField')(default=datetime.date(2012, 1, 9)), keep_default=False)

        # Deleting field 'Notes.content_markdown'
        db.delete_column('notes_notes', 'content_markdown')

        # Deleting field 'Notes.content_html'
        db.delete_column('notes_notes', 'content_html')

        # Deleting field 'Notes.created'
        db.delete_column('notes_notes', 'created')

        # Deleting field 'Notes.modified'
        db.delete_column('notes_notes', 'modified')


    models = {
        'notes.notes': {
            'Meta': {'ordering': "['modified']", 'object_name': 'Notes'},
            'content_html': ('django.db.models.fields.TextField', [], {}),
            'content_markdown': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['notes']
