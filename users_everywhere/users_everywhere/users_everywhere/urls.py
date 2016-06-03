from django.conf.urls import url, include
from django.contrib import admin

from user_management import urls as site_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(site_urls)),
]

