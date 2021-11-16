from django import forms
from booking.models import Appointment


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ("patient",)
        widgets = {
            "content": forms.HiddenInput(),
        }
