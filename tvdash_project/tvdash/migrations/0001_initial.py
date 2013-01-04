# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Genre'
        db.create_table('tvdash_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('tvdash', ['Genre'])

        # Adding model 'MediaFile'
        db.create_table('tvdash_mediafile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=10000, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal('tvdash', ['MediaFile'])

        # Adding M2M table for field related_mediafiles on 'MediaFile'
        db.create_table('tvdash_mediafile_related_mediafiles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_mediafile', models.ForeignKey(orm['tvdash.mediafile'], null=False)),
            ('to_mediafile', models.ForeignKey(orm['tvdash.mediafile'], null=False))
        ))
        db.create_unique('tvdash_mediafile_related_mediafiles', ['from_mediafile_id', 'to_mediafile_id'])

        # Adding M2M table for field genre on 'MediaFile'
        db.create_table('tvdash_mediafile_genre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mediafile', models.ForeignKey(orm['tvdash.mediafile'], null=False)),
            ('genre', models.ForeignKey(orm['tvdash.genre'], null=False))
        ))
        db.create_unique('tvdash_mediafile_genre', ['mediafile_id', 'genre_id'])

        # Adding model 'Movie'
        db.create_table('tvdash_movie', (
            ('mediafile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tvdash.MediaFile'], unique=True, primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=1000, null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('imdb', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('tvdash', ['Movie'])

        # Adding model 'SourceWebsite'
        db.create_table('tvdash_sourcewebsite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=10000, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=1000, null=True, blank=True)),
            ('url_homepage', self.gf('django.db.models.fields.URLField')(max_length=1000)),
            ('url_search', self.gf('django.db.models.fields.URLField')(max_length=2000)),
            ('rating', self.gf('django.db.models.fields.FloatField')(default=1)),
        ))
        db.send_create_signal('tvdash', ['SourceWebsite'])


    def backwards(self, orm):
        # Deleting model 'Genre'
        db.delete_table('tvdash_genre')

        # Deleting model 'MediaFile'
        db.delete_table('tvdash_mediafile')

        # Removing M2M table for field related_mediafiles on 'MediaFile'
        db.delete_table('tvdash_mediafile_related_mediafiles')

        # Removing M2M table for field genre on 'MediaFile'
        db.delete_table('tvdash_mediafile_genre')

        # Deleting model 'Movie'
        db.delete_table('tvdash_movie')

        # Deleting model 'SourceWebsite'
        db.delete_table('tvdash_sourcewebsite')


    models = {
        'tvdash.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'tvdash.mediafile': {
            'Meta': {'object_name': 'MediaFile'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tvdash.Genre']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'related_mediafiles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_mediafiles_rel_+'", 'to': "orm['tvdash.MediaFile']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'tvdash.movie': {
            'Meta': {'object_name': 'Movie', '_ormbases': ['tvdash.MediaFile']},
            'imdb': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mediafile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['tvdash.MediaFile']", 'unique': 'True', 'primary_key': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        'tvdash.sourcewebsite': {
            'Meta': {'object_name': 'SourceWebsite'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rating': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'url_homepage': ('django.db.models.fields.URLField', [], {'max_length': '1000'}),
            'url_search': ('django.db.models.fields.URLField', [], {'max_length': '2000'})
        }
    }

    complete_apps = ['tvdash']