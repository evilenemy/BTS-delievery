from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path("", include(("item.urls", "config"), namespace="item")),
  path("deliever/", include(("deliever.urls", "config"), namespace="deliever")),
  path('admin/', admin.site.urls),
]
