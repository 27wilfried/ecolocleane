
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.conf import settings
from ecolocleaner.settings import MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
]+ static(settings.MEDIA_URL, document_root = MEDIA_ROOT) 
