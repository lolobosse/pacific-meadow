from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views


urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^form', hello.views.form, name='form'),
    url(r'^more', hello.views.more, name='more'),
    path('admin/', admin.site.urls),
]
