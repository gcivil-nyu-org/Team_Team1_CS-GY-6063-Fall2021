from datetime import date
from django.core.validators import MaxValueValidator
from django.db.models.fields import DateField
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from account.models import CustomizedUser
from bootstrap_datepicker_plus import DatePickerInput

class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = "profile.html"
    model = CustomizedUser


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomizedUser
    template_name = "profile_edit.html"
    fields = ["first_name", "last_name", "date_of_birth", "phone_number"]
    success_url = reverse_lazy("profile")
    def get_form(self):
        form = super().get_form()
        form.fields['date_of_birth'].widget = DatePickerInput()
        return form