import django.contrib.auth.views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    url(r'^login/$', auth_views.login,
        {'template_name': 'cabinet/login.html'}, name='login'),
    url(
        r'^logout/$', django.contrib.auth.views.logout,
        {'next_page': '/'}
    ),
    url(r'^register/$', register, name='register'),
]
