from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact_view, name="contact_form"),
    path("contacto_exitoso/", contacto_exitoso, name="contacto_exitoso"),
    path("about/", about, name="about"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", register, name="register"),
]
