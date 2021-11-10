from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required

# from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


# from django.http import HttpResponse

from .models import Appointments, provider_timeSlots


@method_decorator(login_required, name="dispatch")
class BookingUpdateView(UpdateView):
    model = Appointments
    fields = ["user", "status"]
    template_name = "user_appointments"

    def get_success_url(self):
        return reverse_lazy("user_appointments", kwargs={"pk": self.object.pk, }, )

    def get_queryset(self):
        return Appointments.objects.filter(status="confirmed").order_by("date")


def booking(request):
    context = {"appointments": Appointments.objects.all()}
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
