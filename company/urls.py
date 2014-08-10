from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.user_dashboard),
    url(r'^detail/(?P<pk>\d+)/$', views.company_detail),
    url(r'^api/$', views.CompanyApi.as_view()),
    url(r'^api/(?P<pk>\d+)/$', views.CompanyDetailApi.as_view()),
)