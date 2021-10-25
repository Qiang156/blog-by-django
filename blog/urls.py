from django.conf.urls import url
from blog import views

app_name = 'blog'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name="login"),
]