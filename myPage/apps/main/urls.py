__author__ = 'alex'
from django.conf.urls import patterns, url


urlpatterns = patterns('myPage.apps.main.views',
                       url(r'^$','index_view',name="url_index"),
                       )