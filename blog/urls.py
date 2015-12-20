from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'articles/$', views.ArticlesList.as_view()),
    url(r'articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),
]
