# Clinic Appointment & Patient Management System(Group B)
# Team Members:
# Halimatu Sadia Mohammed
# Hanif Olayiwola


# APPOINTMENT CLASS
# Now, this class is basically representing an appointment made by a patient.
# It is going to help us store appointment-related details plus status.
from datetime import datetime, timedelta


class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time, duration, department, purpose,
                 status="Booked"):
        self.appointment_id = appointment_id  # The unique ID for each appointment
        self.patient_id = patient_id  # The ID of the patient who owns this appointment
        self.doctor_id = doctor_id  # The ID of the doctor (UPDATED from 'doctor')
        self.date = date  # Appointment date (format: YYYY-MM-DD)
        self.time = time  # Appointment time (format: HH:MM)
        self.duration = int(duration)  # Duration in minutes (NEW)
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

# PATIENT CLASS
class Patient:
    def __init__(self, patient_id, name, age, contact, gender):
        self.patient_id = patient_id  # Unique ID for each patient (e.g., P001)
        self.name = name  # Full name of the patient
        self.age = int(age)  # Age of the patient
        self.contact = contact  # Phone number
        self.gender = gender  # Gender (Male/Female)

    def __str__(self):
        """Format the patient details for display"""
        return f"{self.patient_id} | {self.name} | Age: {self.age} | Contact: {self.contact} | Gender: {self.gender}"

#DOCTOR CLASS
from datetime import datetime

class Doctor:
    def __init__(self, doctor_id, name, specialty, available_days, start_time, end_time):
        self.doctor_id = doctor_id  # Unique ID for each doctor (e.g., D001)
        self.name = name  # Full name of the doctor
        self.specialty = specialty  # Area of specialization (e.g., Dentistry, Cardiology)
        self.available_days = available_days.split('-')  # Convert "Mon-Tue-Wed" to ['Mon', 'Tue', 'Wed']
        self.start_time = start_time  # When doctor starts work (HH:MM format)
        self.end_time = end_time  # When doctor finishes work (HH:MM format)

    def is_available_on_day(self, date):
        """
        Check if the doctor works on the given date.

        Args:
            date: datetime object or string in YYYY-MM-DD format

        Returns:
            True if doctor works on that day, False otherwise
        """
        # Convert string to datetime if needed
        if isinstance(date, str):
            date = datetime.strptime(date, "%Y-%m-%d")

        # Get the day name (e.g., 'Mon', 'Tue', 'Wed')
        day_name = date.strftime("%a")

        return day_name in self.available_days

    def is_within_working_hours(self, time):
        """
        Check if the given time falls within the doctor's working hours.

        Args:
            time: Time string in HH:MM format

        Returns:
            True if time is within working hours, False otherwise
        """
        return self.start_time <= time <= self.end_time

    def __str__(self):
        """Format the doctor details for display"""
        days = ', '.join(self.available_days)
        return (f"{self.doctor_id} | Dr. {self.name} | {self.specialty} | "
                f"Available: {days} ({self.start_time}-{self.end_time})")


