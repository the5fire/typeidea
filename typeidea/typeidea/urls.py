from django.conf.urls import url
from django.contrib import admin

from .custom_site import custom_site

urlpatterns = [
    url(r'^super_admin/', admin.site.urls),
    url(r'^admin/', custom_site.urls),
]
