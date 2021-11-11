from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from account.models import CustomizedUser


class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = "profile.html"
    model = CustomizedUser


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomizedUser
    template_name = "profile_edit.html"
    fields = ["first_name", "last_name", "date_of_birth", "phone_number"]
    success_url = reverse_lazy("profile")
