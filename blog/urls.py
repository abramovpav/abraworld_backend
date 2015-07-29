from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    url(r'^articles/$', views.articles_list),
    url(r'^articles/(?P<pk>[0-9]+)$', views.article_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
