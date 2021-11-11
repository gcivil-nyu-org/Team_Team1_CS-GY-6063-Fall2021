from booking.models import Appointment
from django.test import TestCase, RequestFactory
from forum.models import CustomizedUser
from booking.views import BookingUpdateView
from datetime import timedelta, date, datetime

# from forum.forms import CommentForm


class BookingUpdateViewTests(TestCase):
    def test_get_queryset(self):
        test_user = CustomizedUser.objects.create_user(
            username="test_user", email="test_user@test_user.com"
        )
        test_doctor = CustomizedUser.objects.create_user(
            username="test_doctor", email="test_doctor@test_doctor.com"
        )
        test_app = Appointment.objects.create(
            user=test_user,
            doctor=test_doctor,
            date=date.today(),
            time=(datetime.now() + timedelta(hours=10)).time(),
            status="confirmed",
        )
        test_app.save()
        request = RequestFactory().get("appointments/" + str(test_app.id))
        request.user = test_user
        view = BookingUpdateView()
        view.request = request
        qs = view.get_queryset()
        self.assertQuerysetEqual(qs, Appointment.objects.all().order_by("date"))
