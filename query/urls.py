from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^query$', views.query, name='query'),
    url(r'^packages$', views.package, name='package')
]