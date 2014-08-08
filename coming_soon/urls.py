from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url('^$', views.Index.as_view()),
)