from django.urls import path
from . import views
from django.contrib.auth import views as as_view

urlpatterns = [
  path("", as_view.LoginView.as_view(template_name="item/login.html"), name="login"),
  path("logout/", as_view.LogoutView.as_view(template_name="item/logout.html"), name="logout"),
  path("signup/", views.sign_up, name="signup"),
  path("home/", views.home, name="home"),
  path("about/", views.about, name="about"),
  path("contact/", views.contact, name="contact"),
]