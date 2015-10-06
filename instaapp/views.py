from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
import datetime

@login_required
def home(request):
    username = request.user.username
    photos = PhotoInstagram.objects.filter()
    return render(request, 'index.html', {'photos': photos, 'username': username})


@login_required
def upload(request, image_id=None):
    image = get_object_or_404(PhotoInstagram, pk=image_id) if image_id else None
    form = ImageForm(instance=image)

    if image and request.user.id != image.user.id:
        return HttpResponse("You does not have permission edit this photo. This photo uploaded by " + request.user.username)

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return HttpResponseRedirect(reverse('instaapp:upload', args=(image.pk,)))
    return render(request, 'upload.html', {'form': form, 'image': image})


@login_required
def photo_view(request, image_id=None):
    if request.method == "POST":
        photo = get_object_or_404(PhotoInstagram, pk=image_id)
        if photo:
            Comment.objects.create(user=request.user, photo=photo, text=request.POST['comment'], created_on=datetime.datetime.utcnow())

    image = get_object_or_404(PhotoInstagram, pk=image_id) if image_id else None
    comments = Comment.objects.filter(photo_id=image_id)
    return render(request, 'photo.html', {'image': image, 'comments': comments})


def login_view(request):
    if request.POST.getlist('login'):
        user = authenticate(username=request.POST['inputUsername'], password=request.POST['inputPassword'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("instaapp:home"))
        else:
            return HttpResponseRedirect(reverse("instaapp:login"))
    return render(request, 'login.html')


def signup_view(request):
    if request.POST.getlist('signup'):
        if request.POST['inputPassword'] != request.POST['inputPassword2']:
            return render(request, 'signup.html')

        user, created = User.objects.get_or_create(username=request.POST['inputUsername'])
        if created:
            user.set_password(request.POST['inputPassword'])
            user.is_active = True
            user.save()
            return HttpResponseRedirect(reverse("instaapp:login"))
        else:
            return render(request, 'signup.html')

    return render(request, 'signup.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("instaapp:home"))