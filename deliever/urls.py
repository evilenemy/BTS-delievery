from django.urls import path
from . import views

urlpatterns = [
  path("items/", views.orders, name="orders"),
  path("order/<int:id>", views.complete_order, name="order_complete"),
  path("profile/<int:id>/", views.view_profile, name="profile")
]