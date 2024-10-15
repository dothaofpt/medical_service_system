
# medical_service/views.py

from django.shortcuts import render, redirect
from django.views import View
from .models import Patient, Doctor, Appointment
from .forms import PatientForm, DoctorForm, AppointmentForm
from django.utils import timezone

class AddPatientView(View):
    def get(self, request):
        form = PatientForm()
        return render(request, 'add_patient.html', {'form': form})

    def post(self, request):
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_patient')
        return render(request, 'add_patient.html', {'form': form})

class AddDoctorView(View):
    def get(self, request):
        form = DoctorForm()
        return render(request, 'add_doctor.html', {'form': form})

    def post(self, request):
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_doctor')
        return render(request, 'add_doctor.html', {'form': form})

class AddAppointmentView(View):
    def get(self, request):
        form = AppointmentForm()
        return render(request, 'add_appointment.html', {'form': form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_appointment')
        return render(request, 'add_appointment.html', {'form': form})

class AppointmentReportView(View):
    def get(self, request):
        appointments = Appointment.objects.all()
        return render(request, 'appointment_report.html', {'appointments': appointments})

class TodayAppointmentsView(View):
    def get(self, request):
        today = timezone.now().date()
        appointments = Appointment.objects.filter(appointment_date__date=today)
        return render(request, 'today_appointments.html', {'appointments': appointments})
