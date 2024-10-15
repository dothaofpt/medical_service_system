# medical_service/forms.py

from django import forms
from .models import Patient, Doctor, Appointment

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['full_name', 'date_of_birth', 'gender', 'address', 'phone_number', 'email']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'specialization', 'phone_number', 'email', 'years_of_experience']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'reason']
