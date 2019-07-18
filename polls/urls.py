from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from django_2 import settings
from . import views
from django.urls import include
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index', views.index),
    url(r'^article', views.article),
    url(r'^detail', views.detail),
    url(r'^message', views.message),
    url(r'^photo', views.photo),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^login', views.login),
    url(r'^register', views.register),
]