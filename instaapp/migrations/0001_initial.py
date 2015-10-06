# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoInstagram',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('image_field', image_cropping.fields.ImageCropField(upload_to='/image/')),
                ('cropping', image_cropping.fields.ImageRatioField('image_field', '120x100', hide_image_field=False, allow_fullsize=True, size_warning=False, help_text=None, adapt_rotation=False, free_crop=False, verbose_name='cropping')),
                ('cropping_free', image_cropping.fields.ImageRatioField('image_field', '300x230', hide_image_field=False, allow_fullsize=False, size_warning=True, help_text=None, adapt_rotation=False, free_crop=True, verbose_name='cropping free')),
            ],
        ),
    ]
