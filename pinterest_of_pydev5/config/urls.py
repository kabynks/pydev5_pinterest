from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("crud.urls")),
    path('', include('django.contrib.auth.urls')),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

