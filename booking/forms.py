from django import forms
from booking.models import Appointment


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ("patient",)
        widgets = {
            "patient": forms.HiddenInput(),
        }

class CancelForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ("status",)
        widgets = {
            "status": forms.HiddenInput(),
        }
