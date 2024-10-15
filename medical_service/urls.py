
# medical_service/urls.py

from django.urls import path
from .views import AddPatientView, AddDoctorView, AddAppointmentView, AppointmentReportView, TodayAppointmentsView

urlpatterns = [
    path('add_patient/', AddPatientView.as_view(), name='add_patient'),
    path('add_doctor/', AddDoctorView.as_view(), name='add_doctor'),
    path('add_appointment/', AddAppointmentView.as_view(), name='add_appointment'),
    path('appointments/report/', AppointmentReportView.as_view(), name='appointment_report'),
    path('appointments/today/', TodayAppointmentsView.as_view(), name='today_appointments'),
]
