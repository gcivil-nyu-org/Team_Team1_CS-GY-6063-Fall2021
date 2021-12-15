from django import forms
from django.core.exceptions import ValidationError
from booking.models import Appointment

import datetime


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
            "date": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%dT",
            ),
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

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        start_time = cleaned_data.get("start_time")
        # start_datetime = datetime.datetime.combine(date, start_time)
        end_time = self.cleaned_data.get("end_time")
        # end_datetime = datetime.datetime.combine(date, end_time)

        if (
            date < datetime.date.today()
            or (date == datetime.date.today() and start_time <= datetime.now().time())
            # or self.start_time <= datetime.datetime.now().time()
            or end_time <= start_time
        ):
            raise ValidationError("Invalid appointment time")
