# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ForeignKey(to='instaapp.PhotoInstagram', related_name='photo')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user')),
            ],
        ),
    ]
