from django.contrib.auth.models import User
from django.db import models
from image_cropping import ImageCropField, ImageRatioField
from taggit.managers import TaggableManager
from annoying.fields import AutoOneToOneField

class UserProfile(models.Model):
    user = AutoOneToOneField('auth.user')
    follows = models.ManyToManyField('UserProfile', related_name='followed_by')

    def __unicode__(self):
        return self.user.username


class PhotoInstagram(models.Model):
    user = models.ForeignKey(User, related_name="uploader")
    image_field = ImageCropField(upload_to='image/')
    cropping = ImageRatioField('image_field', '300x300', allow_fullsize=True)
    # cropping_free = ImageRatioField('image_field', '300x230', free_crop=True, size_warning=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        app_label = 'instaapp'

    def get_cropping_as_list(self):
        if self.cropping:
            return list(map(int, self.cropping.split(',')))


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="user")
    photo = models.ForeignKey(PhotoInstagram, related_name="photo")
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
