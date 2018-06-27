from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'index/$', views.TaskView.as_view(), name='index'),
    url(r'index/login$', views.my_auth, name='login'),
    url(r'success$', views.success_page, name='success')
]