from datetime import date
from django import forms
from django.core.validators import MaxValueValidator
from django.db.models.fields import DateField
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from account.forms import DateInput
from account.models import CustomizedUser

class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = "profile.html"
    model = CustomizedUser


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomizedUser
    template_name = "profile_edit.html"
    fields = ["first_name", "last_name", "date_of_birth", "phone_number"]
    success_url = reverse_lazy("profile")
    widgets = {
            'date_of_birth': DateInput(),
            'date_of_birth': DateField(validators=[MaxValueValidator(limit_value=date.today)]),
            'date_of_birth': forms.DateInput(attrs={'class':'datepicker'}),
        }