from django.conf.urls import include
from django.urls import path
from account.views import (
    IndexView,
    SignUpView,
    # activate,
    # signup,
)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("auth/", include("django.contrib.auth.urls")),
    # path("auth/signup/", signup, name="signup"),
    path("auth/signup/", SignUpView.as_view(), name="signup"),
    # path("activate/<uidb64>/<token>/", activate, name="activate"),
]
