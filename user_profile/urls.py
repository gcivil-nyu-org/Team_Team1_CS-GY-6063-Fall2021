from django.conf.urls import include
from django.urls import path

from user_profile.views import ProfileView, ProfileUpdateView

urlpatterns = [
    path("profile", ProfileView.as_view(), name="profile"),
    path("profile/edit/<int:pk>", ProfileUpdateView.as_view(), name="profile_edit"),
    # path('<str:username>',ProfileView.as_view(),name = 'profile')
]
