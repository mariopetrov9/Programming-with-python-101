from django.contrib import admin
from django.conf.urls import include, url

from courses import urls as website_urls

urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^courses/', include(website_urls)),
    url(r'^home', include(website_urls)),
    url(r'^', include(website_urls)),
]
