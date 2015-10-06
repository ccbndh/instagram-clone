from django.contrib.auth.models import User
from django.db import models
from image_cropping import ImageCropField, ImageRatioField


class PhotoInstagram(models.Model):
    image_field = ImageCropField(upload_to='image/')
    cropping = ImageRatioField('image_field', '120x100', allow_fullsize=True)
    cropping_free = ImageRatioField('image_field', '300x230',
                                    free_crop=True, size_warning=True)

    class Meta:
        app_label = 'instaapp'

    def get_cropping_as_list(self):
        if self.cropping:
            return list(map(int, self.cropping.split(',')))
