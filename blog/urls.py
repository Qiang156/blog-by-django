from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url("index", views.index),
    url(r"(?P<id>\d+)/",views.post_detail),
    url(r"user/<id>\d+", views.user_show),
]