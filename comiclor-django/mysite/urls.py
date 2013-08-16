from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    url(r'^$', views.WelcomeView.as_view(), name="home"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
