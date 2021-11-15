from django.urls import path

from booking.views import (
    PatientAppointmentListView,
    AppointmentCreateView,
    ProviderAppointmentListView,
)

app_name = "booking"

urlpatterns = [
    # path("", views.booking, name="patient-booking"),
    # path("provider_availability", views.timeSlotsView, name="my_availability"),
    # path("addTimeSlot", views.addSlotView, name="addTimeSlot"),
    # path("appointments/<int:pk>", BookingUpdateView.as_view(), name="appointments"),
    path(
        "provider_appointment_list",
        ProviderAppointmentListView.as_view(),
        name="provider_appointment_list",
    ),
    path(
        "patient_appointment_list",
        PatientAppointmentListView.as_view(),
        name="patient_appointment_list",
    ),
    path(
        "new_appointment",
        AppointmentCreateView.as_view(),
        name="new_appointment",
    ),
]
