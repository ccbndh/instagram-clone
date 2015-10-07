# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instaapp', '0004_auto_20151006_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('follows', models.ManyToManyField(related_name='followed_by', to='instaapp.UserProfile')),
                ('user', annoying.fields.AutoOneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
