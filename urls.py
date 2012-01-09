from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webnotes.views.home', name='home'),
    url(r'^notes/', include('notes.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # registration/login.html is the django default - https://docs.djangoproject.com/en/dev/topics/auth/#django.contrib.auth.views.login
    url(r'^login/$', 'django.contrib.auth.views.login'),
    # http://stackoverflow.com/questions/1296629/django-template-tag-how-to-send-next-page-in-url-auth-logout
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/notes/'}),
)

# http://docs.djangoproject.com/en/dev/howto/static-files/#serving-static-files-in-development
from django.conf import settings

if settings.DEBUG :
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )