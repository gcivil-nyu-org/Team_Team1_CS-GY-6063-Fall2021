from datetime import date
from django.core.validators import MaxValueValidator
from django.db.models.fields import DateField
from django.views.generic import UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from account.models import CustomizedUser

from booking.models import Appointment
from forum.models import Post


class ProfileView(LoginRequiredMixin, ListView):
    template_name = "profile.html"
    model = CustomizedUser
    context_object_name = "data"

    def get_queryset(self):
        if self.request.user.is_provider:
            queryset = {
                "upcoming_appointment": Appointment.objects.filter(
                    doctor=self.request.user.id,
                    status="active",
                    patient__isnull=False,
                ).order_by("-date")[:3],
                "newest_post": Post.objects.filter(status="published",author=self.request.user.id).order_by(
                    "-created_at"
                )[:3],
            }

        else:
            queryset = {
                "upcoming_appointment": Appointment.objects.filter(
                    patient=self.request.user.id,
                    status="active",
                ).order_by("-date")[:3],
                "newest_post": Post.objects.filter(status="published",author=self.request.user.id).order_by(
                    "-created_at"
                )[:3],
            }

        return queryset


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomizedUser
    template_name = "profile_edit.html"
    fields = [
        "username",
        "first_name",
        "last_name",
        "date_of_birth",
        "phone_number",
        "profile_img",
    ]
    success_url = reverse_lazy("profile")
    widgets = {
        "date_of_birth": DateField(
            validators=[MaxValueValidator(limit_value=date.today)]
        ),
    }
