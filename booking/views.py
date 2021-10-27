from django.shortcuts import render
from django.http import HttpResponse

from .models import Doctor,Appointments

# Create your views here.


def booking(request):
    context = {
        'appointments': Appointments.objects.all()
    }
    return render(request,'booking/booking.html', context)
    