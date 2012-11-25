# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Book.author_url'
        db.alter_column('books_book', 'author_url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))
        # Adding field 'Category.slug'
        db.add_column('books_category', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Book.author_url'
        db.alter_column('books_book', 'author_url', self.gf('django.db.models.fields.CharField')(default='', max_length=255))
        # Deleting field 'Category.slug'
        db.delete_column('books_category', 'slug')


    models = {
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'author_url': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'book_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'books.category': {
            'Meta': {'object_name': 'Category'},
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['books.Book']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['books']