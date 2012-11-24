# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table('books_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('book_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('author_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('added_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('books', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table('books_book')


    models = {
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'author_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'book_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['books']