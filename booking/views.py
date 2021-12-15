from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from booking.forms import BookForm, CancelForm, ReserveForm
from booking.models import Appointment


@method_decorator(login_required, name="dispatch")
class ProviderAppointmentListView(UserPassesTestMixin, ListView):
    model = Appointment
    template_name = "booking/provider_appointment_list.html"

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user.id).order_by("-date")

    def test_func(self):
        return self.request.user.is_provider


@method_decorator(login_required, name="dispatch")
class AppointmentCreateView(UserPassesTestMixin, CreateView):
    model = Appointment
    template_name = "booking/new_appointment.html"
    form_class = BookForm
    success_url = reverse_lazy("booking:provider_appointment_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        return context

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        return super(AppointmentCreateView, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_provider


@method_decorator(login_required, name="dispatch")
class PatientAppointmentListView(UserPassesTestMixin, ListView):
    model = Appointment
    template_name = "booking/patient_appointment_list.html"
    context_object_name = "appointments"

    def get_queryset(self):
        queryset = {
            "upcoming_appointment": Appointment.objects.filter(
                patient=self.request.user.id,
                status="active",
            ).order_by("date"),
            "available_appointment": Appointment.objects.filter(
                patient__isnull=True,
                status="active",
            ).order_by("-date"),
            "cancelled_appointment": Appointment.objects.filter(
                patient=self.request.user.id,
                status="cancelled",
            ).order_by("-date"),
        }
        return queryset

    def test_func(self):
        return not self.request.user.is_provider


@method_decorator(login_required, name="dispatch")
class PatientReserveView(UserPassesTestMixin, UpdateView):
    model = Appointment
    fields = [
        "patient",
    ]
    reserve_form = ReserveForm()
    template_name = "booking/reserve_appointment.html"
    success_url = reverse_lazy("booking:patient_appointment_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.reserve_form
        context["form"].fields["patient"].initial = self.request.user
        return context

    def test_func(self):
        return not self.request.user.is_provider


@method_decorator(login_required, name="dispatch")
class PatientCancelView(UserPassesTestMixin, UpdateView):
    model = Appointment
    fields = [
        "patient",
    ]
    reserve_form = ReserveForm()
    template_name = "booking/patient_cancel.html"
    success_url = reverse_lazy("booking:patient_appointment_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.reserve_form
        context["form"].fields["patient"].initial = None
        return context

    def test_func(self):
        return not self.request.user.is_provider


@method_decorator(login_required, name="dispatch")
class ProviderCancelView(UserPassesTestMixin, UpdateView):
    model = Appointment
    fields = [
        "status",
    ]
    reserve_form = CancelForm()
    template_name = "booking/provider_cancel.html"
    success_url = reverse_lazy("booking:provider_appointment_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.reserve_form
        context["form"].fields["status"].initial = "cancelled"
        return context

    def test_func(self):
        return self.request.user.is_provider
