from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from vmental.forms import PatientCreationForm
from vmental.forms import ProviderCreationForm


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    form_class = PatientCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")


class ProviderSignUpView(CreateView):
    form_class = ProviderCreationForm
    template_name = 'pro_signup.html'
    success_url = reverse_lazy("pro_login")