

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
