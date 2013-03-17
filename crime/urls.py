from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crime.views.home', name='home'),
    # url(r'^crime/', include('crime.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # These are the new URLs we'll create. More documentation on those here:
    # https://docs.djangoproject.com/en/dev/topics/http/urls/
    # PRO TIP: Copy and paste URL patterns from the above documentation and modify them to fit your needs!
    url('^$', 'data.views.index', name='index'),
    url('^crime/(\d*)/$', 'data.views.detail', name='detail'),
   
)