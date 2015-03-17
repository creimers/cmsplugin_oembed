# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20150306_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=50, blank=True)),
                ('video_url', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
