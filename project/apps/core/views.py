from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import *


def index(request):
    return render(request, "core/index.html")


def contact(request):
    return render(request, "core/contact_form.html")


def about(request):
    return render(request, "core/about.html")


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("core:login")
    else:  # if request.method == "GET":
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})