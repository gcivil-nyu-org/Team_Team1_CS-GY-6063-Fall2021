from django.conf.urls import include, url
from django.urls import path
from vmental.views import IndexView, signup
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("auth/", include("django.contrib.auth.urls")),
    path("auth/signup/", signup, name="signup"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
