from django.urls import path
from booking.views import ProviderAppointmentListView

urlpatterns = [
    # path("", views.booking, name="patient-booking"),
    # path("provider_availability", views.timeSlotsView, name="my_availability"),
    # path("addTimeSlot", views.addSlotView, name="addTimeSlot"),
    # path("appointments/<int:pk>", BookingUpdateView.as_view(), name="appointments"),
    path(
        "prov_appmnt_list",
        ProviderAppointmentListView.as_view(),
        name="prov_appmnt_list",
    ),
]
