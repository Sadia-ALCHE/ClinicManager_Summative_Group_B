# Clinic Appointment & Patient Management System(Group B)
# Team Members:
# Halimatu Sadia Mohammed
# Hanif Olayiwola


# APPOINTMENT CLASS
# Now, this class is basically representing an appointment made by a patient.
# It is going to help us store appointment-related details plus status.
class Appointment:
    def __init__(self, appointment_id, patient_id, date, time, doctor, department, purpose, status="Booked"):
        self.appointment_id = appointment_id  #The unique ID for each appointment
        self.patient_id = patient_id          # The ID of the patient who owns this appointment
        self.date = date                      # Appointment date
        self.time = time                      # Appointment time
        self.doctor = doctor                  # Doctor to meet at the appointment
        self.department = department          # The department/ type of appointment(Dental, X-Ray, etc.)
        self.purpose = purpose                # Purpose of the visit
        self.status = status                  # Status of appointment(Booked or Cancelled)




