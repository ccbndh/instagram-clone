# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('instaapp', '0003_auto_20151006_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoinstagram',
            name='cropping_free',
        ),
        migrations.AddField(
            model_name='photoinstagram',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', verbose_name='Tags', to='taggit.Tag'),
        ),
    ]
