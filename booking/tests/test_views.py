from account.models import CustomizedUser
from booking.models import Appointment
from booking.views import (
    ProviderAppointmentListView,
    PatientAppointmentListView,
    AppointmentCreateView,
    PatientReserveView,
    PatientCancelView,
    ProviderCancelView,
)
from django.test import RequestFactory, TestCase


class ProviderListViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.prov1 = CustomizedUser.objects.create_user(
            username="test_provider1",
            email="test_provider1@email.com",
            is_provider=True,
            date_of_birth="1994-10-10",
        )
        self.prov2 = CustomizedUser.objects.create_user(
            username="test_provider2",
            email="test_provider2@email.com",
            is_provider=True,
            date_of_birth="1994-10-10",
        )

        self.app_1 = Appointment.objects.create(
            date="2021-11-20",
            start_time="9:00:00",
            end_time="12:00:00",
            doctor=self.prov1,
            status="active",
        )
        self.app_1.save()
        self.app_2 = Appointment.objects.create(
            date="2021-11-20",
            start_time="14:00:00",
            end_time="16:00:00",
            doctor=self.prov1,
            status="cancelled",
        )
        self.app_2.save()
        self.app_3 = Appointment.objects.create(
            date="2021-11-21",
            start_time="9:00:00",
            end_time="12:00:00",
            doctor=self.prov2,
            status="active",
        )
        self.app_3.save()
        self.app_4 = Appointment.objects.create(
            date="2021-11-21",
            start_time="9:00:00",
            end_time="12:00:00",
            doctor=self.prov2,
            status="cancelled",
        )
        self.app_4.save()

    def test_get_query_set(self):
        request1 = self.factory.get("/booking/provider_appointment_list")
        request1.user = self.prov1
        view1 = ProviderAppointmentListView()
        view1.request = request1
        qs1 = view1.get_queryset()
        self.assertQuerysetEqual(
            qs1, Appointment.objects.filter(doctor=self.prov1).order_by("-date")
        )
        request2 = self.factory.get("/booking/provider_appointment_list")
        request2.user = self.prov2
        view2 = ProviderAppointmentListView()
        view2.request = request2
        qs2 = view2.get_queryset()
        self.assertQuerysetEqual(
            qs2, Appointment.objects.filter(doctor=self.prov2).order_by("-date")
        )

    def test_test_func(self):
        request = self.factory.get("/booking/provider_appointment_list")
        request.user = self.prov1
        view = ProviderAppointmentListView()
        view.request = request
        self.assertTrue(view.test_func())


class PatientListViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.prov1 = CustomizedUser.objects.create_user(
            username="test_provider1",
            email="test_provider1@email.com",
            is_provider=True,
            date_of_birth="1994-10-10",
        )
        self.prov2 = CustomizedUser.objects.create_user(
            username="test_provider2",
            email="test_provider2@email.com",
            is_provider=True,
            date_of_birth="1994-10-10",
        )
        self.patient1 = CustomizedUser.objects.create_user(
            username="test_patient1",
            email="test_patient1@email.com",
            is_provider=False,
            date_of_birth="1994-10-10",
        )
        self.patient2 = CustomizedUser.objects.create_user(
            username="test_patient2",
            email="test_patient2@email.com",
            is_provider=False,
            date_of_birth="1994-10-10",
        )

        self.app_1 = Appointment.objects.create(
            date="2021-11-20",
            start_time="9:00:00",
            end_time="12:00:00",
            doctor=self.prov1,
            patient=self.patient1,
            status="active",
        )
        self.app_1.save()
        self.app_2 = Appointment.objects.create(
            date="2021-11-20",
            start_time="14:00:00",
            end_time="16:00:00",
            doctor=self.prov1,
            patient=self.patient2,
            status="cancelled",
        )
        self.app_2.save()
        self.app_3 = Appointment.objects.create(
            date="2021-11-21",
            start_time="9:00:00",
            end_time="12:00:00",
            doctor=self.prov2,
            patient=self.patient2,
            status="active",
        )
        self.app_3.save()
        self.app_4 = Appointment.objects.create(
            date="2021-11-21",
            start_time="9:00:00",
            end_time="12:00:00",
            doctor=self.prov2,
            patient=self.patient1,
            status="cancelled",
        )
        self.app_4.save()

    def test_test_func(self):
        request = self.factory.get("/booking/patient_appointment_list")
        request.user = self.patient1
        view = PatientAppointmentListView()
        view.request = request
        self.assertTrue(view.test_func())

    def test_get_query_set(self):
        request1 = self.factory.get("/booking/patient_appointment_list")
        request1.user = self.patient1
        view1 = PatientAppointmentListView()
        view1.request = request1
        qs1 = view1.get_queryset()
        self.assertQuerysetEqual(
            qs1.get("upcoming_appointment"),
            Appointment.objects.filter(patient=self.patient1, status="active").order_by(
                "-date"
            ),
        )
        self.assertQuerysetEqual(
            qs1.get("cancelled_appointment"),
            Appointment.objects.filter(
                patient=self.patient1, status="cancelled"
            ).order_by("-date"),
        )
        request2 = self.factory.get("/booking/patient_appointment_list")
        request2.user = self.patient2
        view2 = PatientAppointmentListView()
        view2.request = request2
        qs2 = view2.get_queryset()
        self.assertQuerysetEqual(
            qs2.get("upcoming_appointment"),
            Appointment.objects.filter(patient=self.patient2, status="active").order_by(
                "-date"
            ),
        )
        self.assertQuerysetEqual(
            qs2.get("cancelled_appointment"),
            Appointment.objects.filter(
                patient=self.patient2, status="cancelled"
            ).order_by("-date"),
        )


class AppointmentCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.prov = CustomizedUser.objects.create_user(
            username="test_provider",
            email="test_provider@email.com",
            is_provider=True,
            date_of_birth="1994-10-10",
        )

    def test_test_func(self):
        request = self.factory.get("/booking/new_appointment")
        request.user = self.prov
        view = AppointmentCreateView()
        view.request = request
        self.assertTrue(view.test_func())

    def test_form_valid(self):
        post_data = {
            "date": "2021-11-20",
            "start_time": "9:00:00",
            "end_time": "12:00:00",
            "doctor": self.prov,
            "status": "active",
        }
        request = self.factory.post(path="booking:new_appointment", data=post_data)
        request.user = self.prov
        response = AppointmentCreateView.as_view()(request)

        self.assertEqual(response.status_code, 200)


class PatientReserveViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.prov = CustomizedUser.objects.create_user(
            username="test_provider",
            email="test_provider@email.com",
            is_provider=True,
            date_of_birth="1994-10-10",
        )
        self.patient = CustomizedUser.objects.create_user(
            username="test_patient",
            email="test_patient@email.com",
            is_provider=False,
            date_of_birth="1994-10-10",
        )
        self.app = Appointment.objects.create(
            date="2021-11-20",
            start_time="9:00:00",
            end_time="12:00:00",
            doctor=self.prov,
            status="active",
        )

    def test_test_func(self):
        request = self.factory.get("/booking/reserve_appointment/", pk=self.app.pk)
        request.user = self.patient
        view = PatientReserveView()
        view.request = request
        self.assertTrue(view.test_func())

    def test_get_context_data(self):
        request = self.factory.get("booking:reserve_appointment", pk=self.app.pk)
        request.user = self.patient
        response = PatientReserveView.as_view()(request, pk=self.app.pk)
        self.assertIsInstance(response.context_data, dict)
        self.assertEqual(len(response.context_data), 4)


class PatientCancelViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.prov = CustomizedUser.objects.create_user(
            username="test_provider",
            email="test_provider@email.com",
            is_provider=True,
            date_of_birth="1994-10-10",
        )
        self.patient = CustomizedUser.objects.create_user(
            username="test_patient",
            email="test_patient@email.com",
            is_provider=False,
            date_of_birth="1994-10-10",
        )
        self.app = Appointment.objects.create(
            date="2021-11-20",
            start_time="9:00:00",
            end_time="12:00:00",
            doctor=self.prov,
            patient=self.patient,
            status="active",
        )

    def test_test_func(self):
        request = self.factory.get("/booking/patient_cacnel/", pk=self.app.pk)
        request.user = self.patient
        view = PatientCancelView()
        view.request = request
        self.assertTrue(view.test_func())

    def test_get_context_data(self):
        request = self.factory.get("booking:patient_cacnel", pk=self.app.pk)
        request.user = self.patient
        response = PatientCancelView.as_view()(request, pk=self.app.pk)
        self.assertIsInstance(response.context_data, dict)
        self.assertEqual(len(response.context_data), 4)


class ProviderCancelViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.prov = CustomizedUser.objects.create_user(
            username="test_provider",
            email="test_provider@email.com",
            is_provider=True,
            date_of_birth="1994-10-10",
        )
        self.patient = CustomizedUser.objects.create_user(
            username="test_patient",
            email="test_patient@email.com",
            is_provider=False,
            date_of_birth="1994-10-10",
        )
        self.app = Appointment.objects.create(
            date="2021-11-20",
            start_time="9:00:00",
            end_time="12:00:00",
            doctor=self.prov,
            patient=self.patient,
            status="active",
        )

    def test_test_func(self):
        request = self.factory.get("/booking/provider_cacnel/", pk=self.app.pk)
        request.user = self.prov
        view = ProviderCancelView()
        view.request = request
        self.assertTrue(view.test_func())

    def test_get_context_data(self):
        request = self.factory.get("booking:provider_cacnel", pk=self.app.pk)
        request.user = self.prov
        response = ProviderCancelView.as_view()(request, pk=self.app.pk)
        self.assertIsInstance(response.context_data, dict)
        self.assertEqual(len(response.context_data), 4)
