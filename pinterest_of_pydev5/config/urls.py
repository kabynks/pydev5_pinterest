from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from crud.models import PostSitemap
from config.settings import MEDIA_URL, MEDIA_ROOT

sitemaps = {
    'static': PostSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("crud.urls")),
    path('', include('django.contrib.auth.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path("profile/", include('accounts.urls'))

]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
