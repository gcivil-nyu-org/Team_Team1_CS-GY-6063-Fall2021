from django.urls import path
from . import views
from booking.views import (
    BookingUpdateView,
    BookingCreateView,
    ProviderAppointmentListView,
)

urlpatterns = [
    path("", views.booking, name="patient-booking"),
    #path("provider_availability", views.timeSlotsView, name="my_availability"),
    #path("provider_availability", name="my_availability"),
    path("addTimeSlot", views.addSlotView, name="addTimeSlot"),
    path("appointments/<int:pk>", BookingUpdateView.as_view(), name="appointments"),
    path("appointments/new/",BookingCreateView.as_view(),name='my_availability'),
    path("appointment_list/", ProviderAppointmentListView.as_view(), name="appointment_list"),
]
