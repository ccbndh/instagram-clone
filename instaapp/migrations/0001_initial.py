# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import instaapp.helpers
import image_cropping.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoInstagram',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('photo', image_cropping.fields.ImageCropField(blank=True, upload_to=instaapp.helpers.item_upload_to)),
                ('cropping', image_cropping.fields.ImageRatioField('photo', '300x300', adapt_rotation=False, free_crop=False, allow_fullsize=False, hide_image_field=True, size_warning=True, help_text=None, verbose_name='cropping')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='uploader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
