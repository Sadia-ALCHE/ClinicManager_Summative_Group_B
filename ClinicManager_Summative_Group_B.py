'''
Clinic Appointment & Patient Management System(Group B)
Team Members:
Halimatu Sadia Mohammed
Hanif Olayiwola '''

import csv
import os
from datetime import datetime, timedelta
# PATIENT CLASS
class Patient:
    """Represents a patient in the clinic system"""

    def __init__(self, patient_id, name, age, contact, gender):
        self.patient_id = patient_id  # Unique ID (e.g., P001)
        self.name = name  # Full name
        self.age = int(age)  # Age
        self.contact = contact  # Phone number
        self.gender = gender  # Gender (Male/Female)

    def __str__(self):
        """Format patient details for display"""
        return f"{self.patient_id} | {self.name} | Age: {self.age} | Contact: {self.contact} | Gender: {self.gender}"

# APPOINTMENT CLASS
'''Represents an appointment of a patient in the clinic system
It is going to help us store appointment-related details plus status. '''
class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time, duration, department, purpose,
                 status="Booked"):
        self.appointment_id = appointment_id  # The unique ID for each appointment
        self.patient_id = patient_id  # Unique ID of the patient(e.g., P001)
        self.doctor_id = doctor_id  # The ID of the doctor (UPDATED from 'doctor')
        self.date = date  # Appointment date (format: YYYY-MM-DD)
        self.time = time  # Appointment time (format: HH:MM)
        self.duration = int(duration)  # Duration in minutes
        self.department = department  # The department/type of appointment (Dental, X-Ray, etc.)
        self.purpose = purpose  # Purpose of the visit
        self.status = status  # Status of appointment (Booked or Cancelled)

    def get_end_time(self):
        """
        Calculate when the appointment ends based on start time and duration.
        Returns: End time as a string in HH:MM format
        """
        start = datetime.strptime(self.time, "%H:%M")
        end = start + timedelta(minutes=self.duration)
        return end.strftime("%H:%M")

    def __str__(self):
        """Format the appointment details for display"""
        end_time = self.get_end_time()
        return (f"{self.appointment_id} | Patient: {self.patient_id} | Doctor: {self.doctor_id} | "
                f"{self.date} {self.time}-{end_time} ({self.duration}min) | "
                f"{self.department} | {self.purpose} | Status: {self.status}")


class Doctor:
    """Represents a doctor in the clinic system"""

    def __init__(self, doctor_id, name, specialty, available_days, start_time, end_time):
        self.doctor_id = doctor_id  # Unique ID (e.g., D001)
        self.name = name  # Doctor's full name
        self.specialty = specialty  # Area of specialization
        self.available_days = available_days.split('-')  # Convert to list
        self.start_time = start_time  # Work start time (HH:MM)
        self.end_time = end_time  # Work end time (HH:MM)

    def is_available_on_day(self, date):
        """Check if doctor works on the given date"""
        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d")
        day_name = date.strftime("%a")
        return day_name in self.available_days

    def is_within_working_hours(self, time):
        """Check if time falls within doctor's working hours"""
        return self.start_time <= time <= self.end_time

    def __str__(self):
        """Format doctor details for display"""
        days = ', '.join(self.available_days)
        return (f"{self.doctor_id} | Dr. {self.name} | {self.specialty} | "
                f"Available: {days} ({self.start_time}-{self.end_time})")

#FILE HANDLING
def load_patients(filename="patients.csv"):
    """Load patient data from CSV file"""
    patients = []

    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                patient = Patient(
                    patient_id=row['patient_id'],
                    name=row['name'],
                    age=row['age'],
                    contact=row['contact'],
                    gender=row['gender']
                )
                patients.append(patient)
        print(f"✓ Loaded {len(patients)} patients from {filename}")

    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with empty patient list.")

    except Exception as e:
        print(f"✗ Error loading patients: {e}")

    return patients


def save_patients(patients, filename="patients.csv"):
    """Save patient data to CSV file"""
    try:
        with open(filename, 'w', newline='') as file:
            fieldnames = ['patient_id', 'name', 'age', 'contact', 'gender']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for patient in patients:
                writer.writerow({
                    'patient_id': patient.patient_id,
                    'name': patient.name,
                    'age': patient.age,
                    'contact': patient.contact,
                    'gender': patient.gender
                })
        print(f"✓ Saved {len(patients)} patients to {filename}")

    except Exception as e:
        print(f"✗ Error saving patients: {e}")


def load_doctors(filename="doctors.csv"):
    """Load doctor data from CSV file"""
    doctors = []

    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                doctor = Doctor(
                    doctor_id=row['doctor_id'],
                    name=row['name'],
                    specialty=row['specialty'],
                    available_days=row['available_days'],
                    start_time=row['start_time'],
                    end_time=row['end_time']
                )
                doctors.append(doctor)
        print(f"✓ Loaded {len(doctors)} doctors from {filename}")

    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with empty doctor list.")

    except Exception as e:
        print(f"✗ Error loading doctors: {e}")

    return doctors


def save_doctors(doctors, filename="doctors.csv"):
    """Save doctor data to CSV file"""
    try:
        with open(filename, 'w', newline='') as file:
            fieldnames = ['doctor_id', 'name', 'specialty', 'available_days', 'start_time', 'end_time']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for doctor in doctors:
                available_days_str = '-'.join(doctor.available_days)
                writer.writerow({
                    'doctor_id': doctor.doctor_id,
                    'name': doctor.name,
                    'specialty': doctor.specialty,
                    'available_days': available_days_str,
                    'start_time': doctor.start_time,
                    'end_time': doctor.end_time
                })
        print(f"✓ Saved {len(doctors)} doctors to {filename}")

    except Exception as e:
        print(f"✗ Error saving doctors: {e}")


def load_appointments(filename="appointments.csv"):
    """Load appointment data from CSV file"""
    appointments = []

    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                appointment = Appointment(
                    appointment_id=row['appointment_id'],
                    patient_id=row['patient_id'],
                    doctor_id=row['doctor_id'],
                    date=row['date'],
                    time=row['time'],
                    duration=row['duration'],
                    department=row['department'],
                    purpose=row['purpose'],
                    status=row['status']
                )
                appointments.append(appointment)
        print(f"✓ Loaded {len(appointments)} appointments from {filename}")

    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with empty appointment list.")

    except Exception as e:
        print(f"✗ Error loading appointments: {e}")

    return appointments


def save_appointments(appointments, filename="appointments.csv"):
    """Save appointment data to CSV file"""
    try:
        with open(filename, 'w', newline='') as file:
            fieldnames = ['appointment_id', 'patient_id', 'doctor_id', 'date', 'time',
                          'duration', 'department', 'purpose', 'status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for appt in appointments:
                writer.writerow({
                    'appointment_id': appt.appointment_id,
                    'patient_id': appt.patient_id,
                    'doctor_id': appt.doctor_id,
                    'date': appt.date,
                    'time': appt.time,
                    'duration': appt.duration,
                    'department': appt.department,
                    'purpose': appt.purpose,
                    'status': appt.status
                })
        print(f"✓ Saved {len(appointments)} appointments to {filename}")

    except Exception as e:
        print(f"✗ Error saving appointments: {e}")

#  CLINIC MANAGER
class ClinicManager:
    def __init__(self):
        self.patients = load_patients()
        self.doctors = load_doctors()
        self.appointments = load_appointments()

    # VALIDATION SECTIONS
    def get_patient_name(self, patient_id):
        for p in self.patients:
            if p.patient_id == patient_id:
                return p.name
        return "Unknown"

    def patient_exists(self, patient_id):
        return any(p.patient_id == patient_id for p in self.patients)

    def doctor_exists(self, doctor_id):
        return any(d.doctor_id == doctor_id for d in self.doctors)

    def get_doctor_by_id(self, doctor_id):
        for d in self.doctors:
            if d.doctor_id == doctor_id:
                return d
        return None

    def check_doctor_availability(self, doctor_id, date, time):
        doctor = self.get_doctor_by_id(doctor_id)

        if not doctor:
            print("Doctor not found")
            return False

        if not doctor.is_available_on_day(date):
            print("Doctor does not work on this day.")
            return False

        if not doctor.is_within_working_hours(time):
            print("Outside doctor's working hours.")
            return False

        return True







