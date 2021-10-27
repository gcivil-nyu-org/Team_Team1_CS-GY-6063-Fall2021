from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from vmental.forms import UserCreationForm
from vmental.models import CustomizedUser

# Create your views here.
class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = "profile.html"
    model = CustomizedUser


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomizedUser
    template_name = "profile_edit.html"
    fields = ["first_name", "last_name", "date_of_birth", "phone_number"]
    success_url = reverse_lazy("profile")
