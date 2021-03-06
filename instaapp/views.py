from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
import datetime
from notifications import notify

@login_required
def home(request):
    username = request.user.username
    photos = PhotoInstagram.objects.filter().order_by('-created')
    return render(request, 'index.html', {'photos': photos, 'username': username})


@login_required
def upload(request, image_id=None):
    image = get_object_or_404(PhotoInstagram, pk=image_id) if image_id else None
    form = ImageForm(instance=image)

    if image and request.user.id != image.user.id:
        return HttpResponse("You does not have permission edit this photo. This photo uploaded by " + image.user.username)

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
        if photo and request.POST.getlist('comment'):
            tags = request.POST['comment']
            for tag in tags.split():
                if tag.startswith("#"):
                    photo.tags.add(tag.strip("#"))

            Comment.objects.create(user=request.user, photo=photo, text=request.POST['comment'], created_on=datetime.datetime.utcnow())
            if int(request.user.id) != int(photo.user.id):
                # notify.send(request.user, recipient=photo.user, verb=request.user.username + ' has comment ' + request.POST['comment']) + ' on your photo'
                comment_add = 'comment_add'
                notify.send(request.user, recipient=photo.user, verb=request.user.username + ' has comment ' + request.POST['comment'] + ' on your photo', action_object=photo, target=photo)

    image = get_object_or_404(PhotoInstagram, pk=image_id) if image_id else None
    comments = Comment.objects.filter(photo_id=image_id)
    return render(request, 'photo.html', {'image': image, 'comments': comments})


@login_required
def profile_view(request):
    following_list = request.user.userprofile.follows.all()
    flollowed_list = request.user.userprofile.followed_by.all()
    photos = PhotoInstagram.objects.filter(user_id=request.user.id)
    return render(request, 'profile.html', {'photos': photos, 'following_list': following_list, 'flollowed_list': flollowed_list})


@login_required
def user_view(request, user_id=None):
    try:
        User.objects.get(id=user_id)
    except:
        return HttpResponse("User not found")

    if request.method == "POST" and request.POST.getlist('follow'):
        if int(request.user.id) == int(user_id):
            return HttpResponse("Yourself")
        try:
            current_user = User.objects.get(id=request.user.id)
            follow_user = User.objects.get(id=user_id)
            current_user.userprofile.follows.add(follow_user.userprofile)
        except:
            pass

    photos = PhotoInstagram.objects.filter(user_id=user_id)
    if request.user.userprofile.follows.all().filter(id=user_id) or int(request.user.id) == int(user_id):
        return render(request, 'user.html', {'photos': photos})

    return render(request, 'user.html', {'photos': photos, 'show_button_follow': '1'})


@login_required
def search_view(request):
    if request.method == "GET" and request.GET.getlist('search'):
        result = PhotoInstagram.objects.filter(tags__name__in=[request.GET['search']])
    return render(request, 'result.html', {'result': result})


def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("instaapp:home"))

    if request.POST.getlist('login'):
        user = authenticate(username=request.POST['inputUsername'], password=request.POST['inputPassword'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("instaapp:home"))
        else:
            return HttpResponseRedirect(reverse("instaapp:login"))
    return render(request, 'login.html')


def signup_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("instaapp:home"))

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