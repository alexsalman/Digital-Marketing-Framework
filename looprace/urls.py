from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from looprace import views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^loop/', include('loop.urls')),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^home/', include('home.urls', namespace='home')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# These two lines work for the admin page
admin.site.site_header = ("Looprace")
admin.site.site_title = ("Looprace")
