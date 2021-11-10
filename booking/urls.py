from django.urls import path
from . import views
from booking.views import BookingUpdateView

urlpatterns = [
    path("", views.booking, name="patient-booking"),
    path("provider-availability", views.doctor_availability, name="provider-availability"),
    path("appointments/<int:pk>", BookingUpdateView.as_view(), name="appointments"),
]
