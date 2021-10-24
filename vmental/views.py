from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from vmental.forms import UserCreationForm
from vmental.models import CustomizedUser


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")

class ProfileView(DetailView, LoginRequiredMixin):
    template_name = 'profile.html'
    model = CustomizedUser
    login_url = 'login'
    # def get_success_url(self):
    #     return reverse('profile', args=[self.request.user.username])
    def get_queryset(self):
        return CustomizedUser.objects.filter(username = 'hahaha')
