from django.conf.urls import url
from blog import views

from blog import views

app_name='blog'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    
    url("index", views.index, name="index"),
    url(r'^category/(?P<category>\w+)/', views.index),
    url(r"^user/(?P<user>\w+)/", views.index),

    url(r'^home/', views.home, name="home"),

    url("edit_post/(?P<pk>\d*)?", views.edit_post, name="edit_post"),
    url(r'^post_list/', views.post_list, name="post_list"),
    url(r'^(?P<pk>\d+)', views.post_detail, name='post_detail'),
    url(r'^getPost/(?P<post_id>\d+)', views.getPost, name="getPost"),
    
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.user_login, name="login"),
    url(r'^logout/', views.user_logout, name='logout'),
]

