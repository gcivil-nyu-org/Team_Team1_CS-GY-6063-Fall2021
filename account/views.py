from django.contrib.auth import get_user_model, login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import CreateView, TemplateView

from account.forms import UserCreationForm
from account.tokens import account_activation_token


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")


# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             message = render_to_string(
#                 "acc_active_email.html",
#                 {
#                     "user": user,
#                     "domain": current_site.domain,
#                     "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                     "token": account_activation_token.make_token(user),
#                 },
#             )
#             mail_subject = "Activate your blog account."
#             to_email = form.cleaned_data.get("email")
#             email = EmailMessage(mail_subject, message, to=[to_email])
#             email.send()
#             return render(request, "email_verify_sent.html", {"form": form})

#     else:
#         form = UserCreationForm()

#     return render(request, "signup.html", {"form": form})


# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         User = get_user_model()
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None:
#         # and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return render(request, "index.html")
#         # return redirect('home')
#         # return 'index'
#     else:
#         return HttpResponse("Activation link is invalid!")
