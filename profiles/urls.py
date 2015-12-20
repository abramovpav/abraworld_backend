from django.conf.urls import url
from profiles import views

urlpatterns = [
    url(r'users/$', views.UsersList.as_view()),
    url(r'users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
    url(r'users/current', views.CurrentUserDetail.as_view()),
    url(r'users/current', views.CurrentUserDetail.as_view()),
]
