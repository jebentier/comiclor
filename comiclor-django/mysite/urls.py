from django.conf.urls import patterns, include, url, defaults
from django.views.generic import TemplateView
from django.contrib import admin

from . import views
from comiclor import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Main Page URLS
    url(r'^$', 'mysite.views.welcome', name='welcome'),
    url(r'^logout$', 'mysite.views.logoff', name='logout'),
    url(r'^register$', 'mysite.views.register_user', name="register"),
    url(r'^confirm_email$', 'mysite.views.confirm_email', name="confim_email"),
    url(r'^update_user$', 'mysite.views.update_user', name="update_user"),

    # Comiclor App URLS
    url(r'^home$', 'comiclor.views.home', name='home'),
    url(r'^library$', 'comiclor.views.library', name='library'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
