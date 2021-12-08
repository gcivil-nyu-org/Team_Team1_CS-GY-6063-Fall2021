from datetime import date
from django.core.validators import MaxValueValidator
from django.db.models.fields import DateField
from django.views.generic import TemplateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from account.models import CustomizedUser
from booking.models import Appointment


class ProfileView(ListView, LoginRequiredMixin):
    template_name = "profile.html"
    model = Appointment
    context_object_name = "appointments"

    def get_queryset(self):
        if self.request.user.is_provider:
            queryset = {
                "upcoming_appointment": Appointment.objects.filter(
                    doctor=self.request.user.id,
                    status="active",
                ).order_by("-date"),
            }
        else:
            queryset = {
                "upcoming_appointment": Appointment.objects.filter(
                    patient=self.request.user.id,
                    status="active",
                ).order_by("-date"),
            }

        return queryset

    # def test_func(self):
    #     return self.request.user.is_provider


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomizedUser
    template_name = "profile_edit.html"
    fields = ["first_name", "last_name", "date_of_birth", "phone_number"]
    success_url = reverse_lazy("profile")
    widgets = {
        "date_of_birth": DateField(
            validators=[MaxValueValidator(limit_value=date.today)]
        ),
    }
