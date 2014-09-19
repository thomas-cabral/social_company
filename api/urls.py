from django.conf.urls import url, patterns

from . import views


urlpatterns = patterns('',
    url(r'^company/$', views.CompanyList.as_view()),
    url(r'^company/(?P<pk>\d+)/$', views.CompanyDetailApi.as_view()),
    url(r'^company/(?P<pk>\d+)/events/$', views.CompanyEventList.as_view()),
)