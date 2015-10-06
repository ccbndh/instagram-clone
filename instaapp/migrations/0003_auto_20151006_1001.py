# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoinstagram',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image_field', '300x300', help_text=None, hide_image_field=False, verbose_name='cropping', free_crop=False, allow_fullsize=True, adapt_rotation=False, size_warning=False),
        ),
    ]
