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





