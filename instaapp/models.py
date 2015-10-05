from django.contrib.auth.models import User
from django.db import models
from image_cropping import ImageCropField, ImageRatioField
from .helpers import *


class PhotoInstagram(models.Model):
    user = models.ForeignKey(User, related_name="uploader")
    title = models.CharField(max_length=120, blank=True, null=True)
    photo = ImageCropField(upload_to=item_upload_to, blank=True)
    cropping = ImageRatioField('photo', '300x300', size_warning=True, hide_image_field=True)
    created = models.DateTimeField(auto_now_add=True)
