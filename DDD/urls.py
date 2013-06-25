from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'DDD.views.basic', name='home'),
    #url(r'^insta/','DDD.views.getNewInstaPost'),

    url(r'^projects/(?P<project>[\w|\W]+)/(?P<page>[\w|\W]+)/$', 'DDD.views.projects'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^basic/', TemplateView.as_view(template_name="basic.html")),
    #(r'^basic/$', Everything.as_view()),
    url(r'^basic','DDD.views.basic', name="basic"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    ###mobile###
    url(r'^about/$', 'DDD.views.about'),
    url(r'^services/$', 'DDD.views.services'),
    url(r'^clients/$', 'DDD.views.clients'),
    url(r'^work/$', 'DDD.views.work'),
    url(r'^works/(?P<project>[\w|\W]+)/(?P<page>[\w|\W]+)/$', 'DDD.views.works'),

)
