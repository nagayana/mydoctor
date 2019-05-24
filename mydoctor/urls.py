from django.conf.urls import url
from . import views

app_name = 'mydoctor'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login_user$', views.index, name='index'),
    url(r'^test_result$', views.test_result, name='test_result'),
    # url(r'^first_login$', views.first_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]

