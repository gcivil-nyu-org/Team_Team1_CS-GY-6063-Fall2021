from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView,CreateView

from booking.models import Appointment, provider_timeSlots


@method_decorator(login_required, name="dispatch")
class BookingUpdateView(UpdateView):
    model = Appointment
    fields = ["patient"]

    def get_success_url(self):
        return reverse_lazy(
            "user_appointments",
            kwargs={
                "pk": self.object.pk,
            },
        )

    #def get_queryset(self):
    #    return Appointment.objects.filter().order_by("date")


def booking(request):
    context = {"appointments": Appointment.objects.all()}
    return render(request, "booking/booking.html", context)


def timeSlotsView(request):
    all_items = provider_timeSlots.objects.all()
    return render(request, "booking/provider_availability.html", {"item": all_items})


def addSlotView(request):
    x = request.POST["date"]
    y = request.POST["time_from"]
    z = request.POST["time_to"]
    new_item = provider_timeSlots(date=x, time_from=y, time_to=z)
    provider_timeSlots.add_to_class(new_item)
    return HttpResponseRedirect("timeSlotsView")



@method_decorator(login_required, name="dispatch")
class BookingCreateView(CreateView):
    model = Appointment
    fields = [
        "date",
        "start_time",
        "end_time",
    ]

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        return super().form_valid(form)
    
