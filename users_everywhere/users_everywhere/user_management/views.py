from django.shortcuts import render, redirect
from .models import User
from django.core.urlresolvers import reverse, reverse_lazy
from .helpers import *
from .decorators import *


@annon_required(redirect_url=reverse_lazy('profile'))
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not user_exists(email):
            User(email=email, password=password).save()
        else:
            error = "User already exists!!!"
    return render(request, 'register.html', locals())


@annon_required(redirect_url=reverse_lazy('profile'))
def login(request):
    if request.method == "POST":
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        if is_logged(email, password):
            request.session['email'] = email
            return redirect(reverse('profile'))
        else:
            error = "Invalid email or password"

    return render(request, 'login.html', locals())


@login_required(redirect_url=reverse_lazy('login'))
def go_to_profile(request):
    email = request.session.get('email')
    if request.method == "POST":
        request.session.flush()
        return redirect(reverse('login'))
    return render(request, 'go_to_profile.html', locals())
