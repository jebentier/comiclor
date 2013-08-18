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
    url(r'^cancel_registration$', 'mysite.views.cancel_registration', name="cancel_registration"),

    # Comiclor App URLS
    url(r'^home$', 'comiclor.views.home', name='home'),
    url(r'^library$', 'comiclor.views.library', name='library'),
    url(r'^cell/new$', 'comiclor.views.cell_creation', name='new_cell'),
    url(r'^content/new$', 'mysite.views.coming_soon', name='new_content'),
    url(r'^comics/books/new$', 'mysite.views.coming_soon', name='new_strip'),
    url(r'^comics/strips/new$', 'mysite.views.coming_soon', name='new_book'),
    url(r'^comics/saved$', 'mysite.views.coming_soon', name='comics_saved'),
    url(r'^search$', 'mysite.views.coming_soon', name='search'),
    url(r'^colaborators$', 'mysite.views.coming_soon', name='colaborators'),
    url(r'^accout$', 'mysite.views.coming_soon', name='account_details'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
