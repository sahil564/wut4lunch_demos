from django.conf.urls import patterns, include, url
from django.contrib import admin
import wut4lunch.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', 'wut4lunch.views.index', name='home'),
    url(r'^newlunch', 'wut4lunch.views.newlunch', name='newlunch'),
)
