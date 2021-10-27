from django.conf.urls import include, url
from django.urls import path
from vmental.views import IndexView, signup
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("auth/", include("django.contrib.auth.urls")),
    path("auth/signup/", signup, name="signup"),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
