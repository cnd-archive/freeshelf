# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('books_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('books', ['Category'])

        # Adding M2M table for field books on 'Category'
        db.create_table('books_category_books', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm['books.category'], null=False)),
            ('book', models.ForeignKey(orm['books.book'], null=False))
        ))
        db.create_unique('books_category_books', ['category_id', 'book_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('books_category')

        # Removing M2M table for field books on 'Category'
        db.delete_table('books_category_books')


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
        },
        'books.category': {
            'Meta': {'object_name': 'Category'},
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['books.Book']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['books']