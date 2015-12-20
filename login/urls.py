from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'auth/login$', views.LoginView.as_view()),
]
