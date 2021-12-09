from django import forms
from booking.models import Appointment

class DateInput(forms.DateInput):
    input_type = 'date'

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


class BookForm(forms.ModelForm):
    class Meta:
        model = Appointment
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%dT",),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
            "end_time": forms.TimeInput(attrs={"type": "time"}),
            "meeting_link": forms.TextInput(attrs={"type": "text"}),
        }
        fields = (
            "date",
            "start_time",
            "end_time",
            "meeting_link",
        )
        
