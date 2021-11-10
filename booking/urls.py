from django.urls import path
from . import views
from booking.views import BookingUpdateView

urlpatterns = [
    path("", views.booking, name="patient-booking"),
    path("provider_availability", views.timeSlotsView, name="my_availability"),
    path("addTimeSlot", views.addSlotView, name = "addTimeSlot"),
    path("appointments/<int:pk>", BookingUpdateView.as_view(), name="appointments"),
]
