from django.conf.urls import url
from . import views

from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)

urlpatterns = [
    # url(r'^$', HomeView.as_view(), name="home"),
    url(r'^login/$', login, {'template_name' : 'integrator/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name' : 'integrator/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, {'post_reset_redirect': 'integrator:password_reset_done'}, name='password_reset'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_collaboration, name='change_collaboration'),
]
