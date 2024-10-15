
from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.full_name

class Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    years_of_experience = models.IntegerField()

    def __str__(self):
        return self.full_name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f"{self.patient.full_name} - {self.doctor.full_name}"
