from django.urls import path

from vmental.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
