from django import forms
from .models import PhotoInstagram


class ImageForm(forms.ModelForm):
    class Meta:
        model = PhotoInstagram
        fields = ('image_field', 'cropping', 'cropping_free')
