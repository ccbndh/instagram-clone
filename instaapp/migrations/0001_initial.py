# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoInstagram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('image_field', image_cropping.fields.ImageCropField(upload_to='image/')),
                ('cropping', image_cropping.fields.ImageRatioField('image_field', '120x100', free_crop=False, verbose_name='cropping', size_warning=False, adapt_rotation=False, hide_image_field=False, allow_fullsize=True, help_text=None)),
                ('cropping_free', image_cropping.fields.ImageRatioField('image_field', '300x230', free_crop=True, verbose_name='cropping free', size_warning=True, adapt_rotation=False, hide_image_field=False, allow_fullsize=False, help_text=None)),
                ('title', models.CharField(null=True, blank=True, max_length=120)),
                ('created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='uploader')),
            ],
        ),
    ]
