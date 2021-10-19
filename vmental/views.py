from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from vmental.forms import PatientCreationForm


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    form_class = PatientCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")
