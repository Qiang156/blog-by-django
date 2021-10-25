from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url("index", views.index, name="index"),
    url("edit_post/(?P<pk>\d*)?", views.edit_post, name="edit_post"),
]