'''
Clinic Appointment & Patient Management System(Group B)
Team Members:
Halimatu Sadia Mohammed
Hanif Olayiwola
'''

import csv
from datetime import datetime, timedelta
# PATIENT CLASS
class Patient:
    """Represents a patient in the clinic system
    This class stores all patient information including their unique ID,
    personal details, and contact information. Each patient object represents
    one row in the patients.csv file.
    """

    def __init__(self, patient_id, name, age, contact, gender):
        self.patient_id = patient_id  # Unique ID (e.g., P001)
        self.name = name  # Full name
        self.age = int(age)  # Convert age to integer
        self.contact = contact  # Phone number
        self.gender = gender  # Gender (Male/Female)

    def __str__(self):
        """Format patient details for display"""
        return f"{self.patient_id} | {self.name} | Age: {self.age} | Contact: {self.contact} | Gender: {self.gender}"


# APPOINTMENT CLASS
''' Represents an appointment of a patient in the clinic system
It is going to help us store appointment-related details plus status. '''
class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time, duration, department, purpose,
                 status="Booked"):
        self.appointment_id = appointment_id  # The unique ID for each appointment
        self.patient_id = patient_id  # Unique ID of the patient(e.g., P001)
        self.doctor_id = doctor_id  # The ID of the doctor(e.g., D001)
        self.date = date  # Appointment date (format: YYYY-MM-DD)
        self.time = time  # Appointment time (format: HH:MM)
        self.duration = int(duration)  # Duration of appointment
        self.department = department  # The department/type of appointment (Dental, X-Ray, etc.)
        self.purpose = purpose  # Purpose of the visit
        self.status = status  # Status of appointment (Booked or Cancelled)

    def get_end_time(self):
        """
        Calculate when the appointment ends based on start time and duration.
        Returns: End time as a string in HH:MM format
        """
        # Convert start time string to datetime object
        start = datetime.strptime(self.time, "%H:%M")
        # Add duration to get end time
        end = start + timedelta(minutes=self.duration)
        # Convert back to string format
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
        # Get day name (Mon, Tue, etc.)
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
    patients = [] # Initialize empty list

    try:
        # Open file for reading
        with open(filename, 'r') as file:
            reader = csv.DictReader(file) # Read CSV with headers
            # Loop through each row
            for row in reader:
                # Create Patient object from row data
                patient = Patient(
                    patient_id=row['patient_id'],
                    name=row['name'],
                    age=row['age'],
                    contact=row['contact'],
                    gender=row['gender']
                )
                patients.append(patient) # Add to list

    except FileNotFoundError:
        # File doesn't exist yet (first run)
        print(f"Warning: {filename} not found. Starting with empty patient list.")

    except Exception as e:
        # Catch any other errors
        print(f"Error loading patients: {e}")

    return patients # Return list (empty or filled)


def save_patients(patients, filename="patients.csv"):
    """Save patient data to CSV file"""
    try:
        # Open file for writing (overwrites existing)
        with open(filename, 'w', newline='') as file:
            fieldnames = ['patient_id', 'name', 'age', 'contact', 'gender'] # Define columns
            writer = csv.DictWriter(file, fieldnames=fieldnames) # Create CSV writer

            writer.writeheader()   # Write column headers
            # Write each patient as a row
            for patient in patients:
                writer.writerow({
                    'patient_id': patient.patient_id,
                    'name': patient.name,
                    'age': patient.age,
                    'contact': patient.contact,
                    'gender': patient.gender
                })

    except Exception as e:
        print(f"Error saving patients: {e}")


def load_doctors(filename="doctors.csv"):
    """Load doctor data from CSV file"""
    doctors = [] # Initialize empty list

    try:
        with open(filename, 'r') as file: # Open for reading
            reader = csv.DictReader(file) # Read with headers

            for row in reader: # Loop through rows
                # Create Doctor object from row
                doctor = Doctor(
                    doctor_id=row['doctor_id'],
                    name=row['name'],
                    specialty=row['specialty'],
                    available_days=row['available_days'],
                    start_time=row['start_time'],
                    end_time=row['end_time']
                )
                doctors.append(doctor) # Add to list

    except FileNotFoundError:
        print(f"Warning: {filename} not found. Starting with empty doctor list.")

    except Exception as e:
        print(f"✗ Error loading doctors: {e}")

    return doctors


def save_doctors(doctors, filename="doctors.csv"):
    """Save doctor data to CSV file"""
    try:
        with open(filename, 'w', newline='') as file: # Open for writing
            fieldnames = ['doctor_id', 'name', 'specialty', 'available_days', 'start_time', 'end_time']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader() # Write headers
            for doctor in doctors: # Loop through doctors
                available_days_str = '-'.join(doctor.available_days) # Convert list to string
                writer.writerow({
                    'doctor_id': doctor.doctor_id,
                    'name': doctor.name,
                    'specialty': doctor.specialty,
                    'available_days': available_days_str,
                    'start_time': doctor.start_time,
                    'end_time': doctor.end_time
                })

    except Exception as e:
        print(f"✗ Error saving doctors: {e}")


def load_appointments(filename="appointments.csv"):
    """Load appointment data from CSV file"""
    appointments = [] # Initialize empty list

    try:
        with open(filename, 'r') as file: # Open for reading
            reader = csv.DictReader(file)
            for row in reader: # Loop through rows
                # Create Appointment object
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

            writer.writeheader() # Write column headers
            for appt in appointments: # Loop through appointments
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

    except Exception as e:
        print(f"Error saving appointments: {e}")

#  CLINIC MANAGER
class ClinicManager:
    def __init__(self):
        # Load all data from CSV files
        self.patients = load_patients()
        self.doctors = load_doctors()
        self.appointments = load_appointments()

    # VALIDATION SECTIONS
    def get_patient_name(self, patient_id):
        # Loop through all patients
        for p in self.patients:
            if p.patient_id == patient_id:
                return p.name # Return name if found
        return "Unknown" # Return default if not found

    def patient_exists(self, patient_id):
        # Return True if any patient has this ID
        return any(p.patient_id == patient_id for p in self.patients)

    def doctor_exists(self, doctor_id):
        # Return True if any doctor has this ID
        return any(d.doctor_id == doctor_id for d in self.doctors)

    def get_doctor_by_id(self, doctor_id):
        # Loop through doctors
        for d in self.doctors:
            if d.doctor_id == doctor_id:
                return d
        return None

    def check_doctor_availability(self, doctor_id, date, time):
        doctor = self.get_doctor_by_id(doctor_id) # Get doctor object
        # Check if doctor exists
        if not doctor:
            print("Doctor not found")
            return False
        # Check if doctor works on this day
        if not doctor.is_available_on_day(date):
            print("Doctor does not work on this day.")
            return False
        # Check if time is within working hours
        if not doctor.is_within_working_hours(time):
            print("Outside doctor's working hours.")
            return False

        return True # All checks passed

    def slot_available(self, doctor_id, date, time, duration):
        ''' Check for overlapping appointments using duration '''
        new_start = datetime.strptime(time, "%H:%M")
        new_end = new_start + timedelta(minutes=duration)
        # Check all existing appointments
        for a in self.appointments:
            # Only check same doctor, same date, active appointments
            if a.doctor_id == doctor_id and a.date == date and a.status == "Booked":
                existing_start = datetime.strptime(a.time, "%H:%M")
                existing_end = existing_start + timedelta(minutes=a.duration)
                # Overlap check
                if new_start < existing_end and new_end > existing_start:
                    return False
        return True

    # PATIENT MANAGEMENT
    def add_patient(self):
        """Register a new patient"""
        print("\n=== Register New Patient ===")

        # Generate new patient ID
        if self.patients:
            last_id = self.patients[-1].patient_id # Get last patient ID
            id_number = int(last_id[1:]) + 1 # Extract number and increment
            patient_id = f"P{id_number:03d}" # Format with leading zeros
        else:
            patient_id = "P001" # First patient

        print(f"New Patient ID: {patient_id}")

        # Get patient name
        name = input("Enter patient name: ").strip()
        if not name: # Validate not empty
            print("Error: Name cannot be empty")
            return
        # Get and validate age
        try:
            age = int(input("Enter age: ")) # Convert to integer
            if age <= 0 or age > 120: # Check reasonable range
                print("Error: Invalid age")
                return
        except ValueError: # Handle non-numeric input
            print("Error: Age must be a number")
            return
        # Get contact number
        contact = input("Enter contact number: ").strip()
        if not contact:
            print("Error: Contact cannot be empty")
            return
        # Get and validate gender
        gender = input("Enter gender (Male/Female): ").strip()
        if gender not in ["Male", "Female"]:
            print("✗ Error: Gender must be Male or Female")
            return

        # Create and add patient
        new_patient = Patient(patient_id, name, age, contact, gender)
        self.patients.append(new_patient) # Add to list

        # Save to CSV
        save_patients(self.patients)

        print(f"\n Patient registered successfully!")
        print(new_patient)

    def search_patient(self):
        """Search for a patient by ID or name"""
        print("\n=== Search Patient ===")
        search_term = input("Enter Patient ID or Name: ").strip()

        if not search_term:
            print(" Error: Search term cannot be empty")
            return

        found_patients = [] # Store results

        # Search by ID or name
        for patient in self.patients:
            # Check if matches ID (exact) or name (partial, case-insensitive)
            if (search_term.upper() == patient.patient_id.upper() or
                    search_term.lower() in patient.name.lower()):
                found_patients.append(patient)

        # Display results
        if found_patients:
            print(f"\n Found {len(found_patients)} patient(s):")
            print("-" * 80)
            for patient in found_patients:
                print(patient)
            print("-" * 80)
        else:
            print(f" No patients found matching '{search_term}'")

    def show_patients(self):
        """Display all patient records"""
        if not self.patients: # Check if empty
            print("\n No patients in the system")
            return

        print(f"\n=== All Patients ({len(self.patients)} total) ===")
        print("-" * 80)
        # Print table header with column alignment
        print(f"{'ID':<8} {'Name':<25} {'Age':<5} {'Contact':<15} {'Gender':<10}")
        print("-" * 80)

        # Print each patient as a row
        for patient in self.patients:
            print(f"{patient.patient_id:<8} {patient.name:<25} {patient.age:<5} "
                  f"{patient.contact:<15} {patient.gender:<10}")

        print("-" * 80)

    # DOCTOR MANAGEMENT
    def show_doctors(self):
        """Display all doctors"""
        if not self.doctors: # Check if empty
            print("\n No doctors in the system")
            return

        print(f"\n=== All Doctors ({len(self.doctors)} total) ===")
        print("-" * 100)
        # Print table header
        print(f"{'ID':<8} {'Name':<25} {'Specialty':<20} {'Available Days':<20} {'Hours':<15}")
        print("-" * 100)
        # Print each doctor as a row
        for doctor in self.doctors:
            days = ', '.join(doctor.available_days)
            hours = f"{doctor.start_time}-{doctor.end_time}"
            print(f"{doctor.doctor_id:<8} {doctor.name:<25} {doctor.specialty:<20} "
                  f"{days:<20} {hours:<15}")

        print("-" * 100)

    def search_doctor(self):
        """Search for doctors by ID, name, or specialty"""
        print("\n=== Search Doctor ===")
        print("Search by:")
        print("1. Doctor ID")
        print("2. Doctor Name")
        print("3. Specialty")

        choice = input("Choose search type (1-3): ").strip()

        if choice not in ["1", "2", "3"]: # Validate choice

            print(" Invalid choice")
            return

        search_term = input("Enter search term: ").strip()

        if not search_term:
            print(" Error: Search term cannot be empty")
            return

        found_doctors = [] # Store results

        # Search based on choice
        for doctor in self.doctors:
            if choice == "1":  # Search by ID
                if search_term.upper() == doctor.doctor_id.upper():
                    found_doctors.append(doctor)
            elif choice == "2":  # Search by name
                if search_term.lower() in doctor.name.lower():
                    found_doctors.append(doctor)
            elif choice == "3":  # Search by specialty
                if search_term.lower() in doctor.specialty.lower():
                    found_doctors.append(doctor)

        # Display results
        if found_doctors:
            print(f"\nFound {len(found_doctors)} doctor(s):")
            print("-" * 100)
            for doctor in found_doctors:
                print(doctor)
            print("-" * 100)
        else:
            print(f"✗ No doctors found matching '{search_term}'")

    # APPOINTMENT MANAGEMENT
    def book_appointment(self):
        try: # Get and validate patient ID
            patient_id = input("Enter patient ID: ")
            if not self.patient_exists(patient_id):
                print("Patient not found. Please register patient first.")
                return

            print("\nAvailable Doctors:")
            self.show_doctors()
            # Get and validate doctor ID
            doctor_id = input("Enter doctor ID: ")
            if not self.doctor_exists(doctor_id):
                print("Doctor not found.")
                return

            print("Appointment Types:")
            print("1. Dental (30 mins)")
            print("2. X-Ray (20 mins)")
            print("3. Physio (45 mins)")
            print("4. General Consultation (30 mins)")

            type_choice = input("Choose appointment type: ")

            if type_choice == "1":
                department, duration = "Dental", 30
            elif type_choice == "2":
                department, duration = "X-Ray", 20
            elif type_choice == "3":
                department, duration = "Physio", 45
            elif type_choice == "4":
                department, duration = "General Consultation", 30
            else:
                print("Invalid choice.")
                return

            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            purpose = input("Enter purpose: ")

            # Check doctor availability
            if not self.check_doctor_availability(doctor_id, date, time):
                return
            # Check for time conflicts
            if not self.slot_available(doctor_id, date, time, duration):
                print("Time slot is already booked.")
                return

            # Generate appointment ID
            if self.appointments:
                last_id = self.appointments[-1].appointment_id
                number = int(last_id[1:]) + 1
                appointment_id = f"A{number:03d}"
            else:
                appointment_id = "A001"
            # Create and add appointment
            self.appointments.append(
                Appointment(
                    appointment_id,
                    patient_id,
                    doctor_id,
                    date,
                    time,
                    duration,
                    department,
                    purpose
                )
            )
            # Save to file
            save_appointments(self.appointments)
            print("Appointment booked successfully.")

        except ValueError: # Handle conversion errors
            print("Invalid input.")

    def cancel_appointment(self):
        try:
            appointment_id = input("Enter appointment ID: ")
            for a in self.appointments: # Search for appointment
                if a.appointment_id == appointment_id:
                   a.status = "Cancelled" # Update status
                   save_appointments(self.appointments) # Save changes
                   print("Appointment cancelled successfully.")
                   return
            print("Appointment not found.")
        except Exception as e:
            print(f"Error: {e}")

    def reschedule_appointment(self):
        try:
            patient_id = input("Enter patient ID: ")
            # Get all active appointments for this patient
            patient_apps = [
                a for a in self.appointments
                if a.patient_id == patient_id and a.status == "Booked"
            ]

            if not patient_apps: # Check if patient has any active appointments
                print("No active appointments for this patient.")
                return
            # Display patient's appointments
            print("\nAppointment ID | Patient ID | Date | Time | Doctor | Department | Purpose")
            print("-" * 65)
            for a in patient_apps:
                print(
                    f"{a.appointment_id} | {a.patient_id} | {a.date} | {a.time} | "
                    f"{a.doctor_id} | {a.department} | {a.purpose}"
                )
            # Get appointment to reschedule
            appointment_id = input("\nEnter appointment ID to reschedule: ")

            # Find the specific appointment first
            target_appointment = None
            for a in self.appointments:
                if a.appointment_id == appointment_id and a.status == "Booked":
                    target_appointment = a
                    break
            # Check if appointment found
            if not target_appointment:
                print("Appointment not found or already cancelled.")
                return

            new_date = input("Enter new date (YYYY-MM-DD): ")
            new_time = input("Enter new time (HH:MM): ")

            # Check availability
            if not self.check_doctor_availability(target_appointment.doctor_id, new_date, new_time):
                return

            if not self.slot_available(target_appointment.doctor_id, new_date, new_time, target_appointment.duration):
                print("Time slot is already booked.")
                return

            # Update the appointment
            target_appointment.date = new_date
            target_appointment.time = new_time
            save_appointments(self.appointments)
            print("Appointment rescheduled successfully.")

            print("Appointment not found.")

        except ValueError:
            print("Invalid input.")

    def show_appointments(self):
        if not self.appointments:
            print("No appointments found.")
            return

        print("\nAppointment ID | Patient | Doctor | Date | Time | Department | Status")
        print("-" * 100)

        for a in self.appointments:
            patient_name = self.get_patient_name(a.patient_id)

            print(
                f"{a.appointment_id} | {patient_name} | "
                f"{a.doctor_id} | {a.date} | "
                f"{a.time}-{a.get_end_time()} | "
                f"{a.department} | {a.status}"
            )

    def search_appointment(self):
        print("\nSearch appointment by:")
        print("1. Patient ID")
        print("2. Doctor ID")

        choice = input("Enter choice (1 or 2): ").strip()

        results = []

        if choice == "1":
            patient_id = input("Enter patient ID: ").strip()
            results = [a for a in self.appointments if a.patient_id == patient_id]

        elif choice == "2":
            doctor_id = input("Enter doctor ID: ").strip()
            results = [a for a in self.appointments if a.doctor_id == doctor_id]

        else:
            print("Invalid choice.")
            return

        if not results:
            print("No matching appointments found.")
            return

        print("\nAppointment ID | Patient | Doctor | Date | Time | Department | Status")
        print("-" * 75)

        for a in results:
            patient_name = self.get_patient_name(a.patient_id)
            print(
                f"{a.appointment_id} | {patient_name} | {a.doctor_id} | "
                f"{a.date} | {a.time}-{a.get_end_time()} | "
                f"{a.department} | {a.status}"
            )

# MAIN MENU

def main():
    """Main menu for the clinic management system"""
    system = ClinicManager()

    while True:
        print("\n" + "=" * 50)
        print("   CLINIC APPOINTMENT & PATIENT MANAGEMENT SYSTEM  ")
        print("=" * 50)
        print("\n--- Patient Management ---")
        print("1. Add Patient")
        print("2. Search Patient")
        print("3. Show All Patients")
        print("\n--- Doctor Management ---")
        print("4. Show All Doctors")
        print("5. Search Doctor")
        print("\n--- Appointment Management ---")
        print("6. Book Appointment")
        print("7. Cancel Appointment")
        print("8. Reschedule Appointment")
        print("9. Show All Appointments")
        print("10. Search Appointments")
        print("\n0. Exit")
        print("=" * 50)

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            system.add_patient()
        elif choice == "2":
            system.search_patient()
        elif choice == "3":
            system.show_patients()
        elif choice == "4":
            system.show_doctors()
        elif choice == "5":
            system.search_doctor()
        elif choice == "6":
            system.book_appointment()
        elif choice == "7":
            system.cancel_appointment()
        elif choice == "8":
            system.reschedule_appointment()
        elif choice == "9":
            system.show_appointments()
        elif choice == "10":
            system.search_appointment()
        elif choice == "0":
            print("\nThank you for using Clinic Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()