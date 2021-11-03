from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


# from django.http import HttpResponse

from .models import Appointments

@method_decorator(login_required, name="dispatch")

class BookingUpdateView(UpdateView):
    model = Appointments
    fields = ["user", "status"]
    template_name = "user_appointments"

    def get_success_url(self):
        return reverse_lazy(
            "user_appointments",
            kwargs={
                "pk": self.object.pk,

            },
        )
 
    def get_queryset(self):
        return Appointments.objects.filter(status='confirmed').order_by("date")






def booking(request):
    context = {"appointments": Appointments.objects.all()}
    return render(request, "booking/booking.html", context)
