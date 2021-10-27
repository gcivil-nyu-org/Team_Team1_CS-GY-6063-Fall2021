from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
appointments = [
    {
        'date': '29 Oct 2021',
        'day': 'Thursday',
        'time': '9:00 pm',
        'location': 'ABC Place',
        'status': 'unbooked',
    },
    {
        'date': '29 Oct 2021',
        'day': 'Thursday',
        'time': '10:00 pm',
        'location': 'XYZ Place',
        'status': 'unbooked',
    },
    {
        'date': '30 Oct 2021',
        'day': 'Friday',
        'time': '9:00 pm',
        'location': 'PQR Place',
        'status': 'unbooked',
    },
]

def booking(request):
    context = {
        'appointments': appointments
    }
    return render(request,'booking/booking.html', context)
    