from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'social_company.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('coming_soon.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^company/', include('company.urls', namespace='company')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )