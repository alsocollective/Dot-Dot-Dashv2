from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'DDD.views.home', name='home'),
    #url(r'^insta/','DDD.views.getNewInstaPost'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^basic/', TemplateView.as_view(template_name="basic.html")),
    #(r'^basic/$', Everything.as_view()),
    url(r'^basic','DDD.views.basic', name="basic"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
