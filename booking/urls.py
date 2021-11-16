from django.urls import path

from booking.views import (
    AppointmentCreateView,
    PatientAppointmentListView,
    PatientCancelView,
    PatientReserveView,
    ProviderAppointmentListView,
)

app_name = "booking"

urlpatterns = [
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
    path(
        "reserve_appointment/<int:pk>",
        PatientReserveView.as_view(),
        name="reserve_appointment",
    ),
    path(
        "patient_cancel/<int:pk>",
        PatientCancelView.as_view(),
        name="patient_cancel",
    ),
]
