from django.contrib import admin
from django.urls import include, path

from vmental.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]