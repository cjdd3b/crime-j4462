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

    ########## CRIME PROJECT URLS BEGIN HERE ##########

    # These are the new URLs we'll create. More documentation on those here:
    # https://docs.djangoproject.com/en/dev/topics/http/urls/
    
    url('^$', 'data.views.index', name='index'),

    url('^crime/(\d*)/$', 'data.views.detail', name='detail'), # Note the trailing comma. ALWAYS ADD ONE AFTER EVERY URL.
   
    # Whoa! What's with the weird (\d*/$) notation? These are called "regular expressions" and
    # you can read more about them here: http://www.tutorialspoint.com/python/python_reg_expressions.htm

    # That said, you have two choices in dealing with these. The first is to actually learn them, which is
    # a great thing to do but definitely comes with a learning curve. That said, it will allow you to do all
    # sorts of cool text-parsing tasks that are going to come in handy someday.

    # The other option -- and the one I prefer -- is to copy and paste from the URLs documentation above.
)