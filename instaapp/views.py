from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def home(request):
    return render(request, 'index.html')


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