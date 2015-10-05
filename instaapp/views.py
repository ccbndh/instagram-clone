from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'index.html')


def login_view(request):
    if request.POST.getlist('login'):
        user = authenticate(username=request.POST['inputEmail'], password=request.POST['inputPassword'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("instaapp:home"))
        else:
            return HttpResponseRedirect(reverse("instaapp:login"))
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("instaapp:home"))