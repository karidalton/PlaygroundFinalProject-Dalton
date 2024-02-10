from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import *


def index(request):
    return render(request, "core/index.html")


def contact(request):
    return render(request, "core/contact_form.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "core/about.html")


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {"form": form})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:contacto_exitoso')
    else:
        form = ContactForm()
    return render(request, 'core/contact_form.html', {'form': form})


def contacto_exitoso(request):
    return render(request, "core/contacto_exitoso.html")
