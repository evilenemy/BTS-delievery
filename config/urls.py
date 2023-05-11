from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path("", include(("item.urls", "config"), namespace="item")),
  path("deliever/", include(("deliever.urls", "config"), namespace="deliever")),
  path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
