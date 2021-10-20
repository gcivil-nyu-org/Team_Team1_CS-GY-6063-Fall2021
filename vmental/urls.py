from django.conf.urls import include
from django.urls import path

from vmental.views import IndexView, SignUpView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/signup/', SignUpView.as_view(), name='signup')
]
