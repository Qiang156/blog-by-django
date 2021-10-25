from django.conf.urls import url

from blog import views

app_name='blog'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url("index", views.index),

    url(r'^post_list/', views.post_list, name="post_list"),

    url(r'^(?P<pk>\d+)', views.post_detail, name='post_detail'),
    url(r'^getPost/(?P<post_id>\d+)', views.getPost, name="getPost"),

    url(r"user/<id>\d+", views.user_show),
]