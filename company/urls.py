from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.user_dashboard),
    url(r'^detail/(?P<pk>\d+)/$', views.company_detail),
)