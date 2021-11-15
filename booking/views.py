from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView

from booking.models import Appointment


@method_decorator(login_required, name="dispatch")
class ProviderAppointmentListView(UserPassesTestMixin, ListView):
    model = Appointment
    template_name = "prov_appmnt_list"

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user.id)

    def test_func(self):
        return self.request.user.is_provider


# @method_decorator(login_required, name="dispatch")
# class BookingUpdateView(UpdateView):
#     model = Appointment
#     fields = ["user", "status"]
#     template_name = "user_appointments"

#     def get_success_url(self):
#         return reverse_lazy(
#             "user_appointments",
#             kwargs={
#                 "pk": self.object.pk,
#             },
#         )

#     def get_queryset(self):
#         return Appointment.objects.filter(status="confirmed").order_by("date")


# def booking(request):
#     context = {"appointments": Appointment.objects.all()}
#     return render(request, "booking/booking.html", context)


# def timeSlotsView(request):
#     all_items = provider_timeSlots.objects.all()
#     return render(request, "booking/provider_availability.html", {"item": all_items})


# def addSlotView(request):
#     x = request.POST["date"]
#     y = request.POST["time_from"]
#     z = request.POST["time_to"]
#     new_item = provider_timeSlots(date=x, time_from=y, time_to=z)
#     provider_timeSlots.add_to_class(new_item)
#     return HttpResponseRedirect("timeSlotsView")
