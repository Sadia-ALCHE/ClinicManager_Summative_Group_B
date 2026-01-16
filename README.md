Clinic Appointment & Patient Management System (Group B)

Project Overview:
This project is a console-based Clinic Appointment & Patient Management System developed in Python. It is designed to understand and demonstrate core programming concepts such as:
- Object-Oriented Programming (OOP)
- File handling using CSV files
- Input validation
- Basic scheduling logic

The system allows a clinic to manage patients, doctors, and appointments efficiently through a menu-driven interface.

Team Members:
- Halimatu Sadia Mohammed
- Hanif Olayiwola

Technologies Used:
- Python 3
- CSV files for storage
- datetime module for date and time handling

Project Structure:
ClinicManager_Summative_Group_B:
- patients.csv        # Stores patient records
- doctors.csv         # Stores doctor records
- appointments.csv    # Stores appointment records
- main.py             # Main Python program
- README.md           # Project documentation

Data Storage (CSV Files):
The system uses CSV files to store data persistently:
- patients.csv         # Stores patient details
- doctors.csv          # Stores doctor details
- appointments.csv     # Stores appointment records
The system automatically:
- Loads data on startup
- Saves data after any update

System Design (Classes):
1. Patient Class: Represents a patient in the clinic.
Attributes:
- patient_id
- name
- age
- contact
- gender
This helps us to store and display patient information.

2. Doctor Class: Represents a doctor working in the clinic.
Attributes:
- doctor_id
- name
- specialty
- available_days
- start_time
- end_time
This helps us to handle the doctor's availability and working hours.

3. Appointment Class: Represents an appointment booking.
Attributes:
- appointment_id
- patient_id
- doctor_id
- date
- time
- duration
- department
- purpose
- status
This helps us to manage appointment scheduling, duration, and status.

4. ClinicManager Class: This is the core controller class of the system.
Responsibilities:
- Load and save data from CSV files
- Validate patients and doctors
- Manage patients, doctors, and appointments
- Prevent appointment clashes

System Functionalities:
A. Patient Management
- Add new patient
- Search patient by ID or name
- Display all patients

B. Doctor Management
- Display all doctors
- Search doctor by ID, name, or specialty

C. Appointment Management
- Book appointment
- Cancel appointment
- Reschedule appointment
- View all appointments
- Search appointments by patient or doctor














These files are automatically created or updated when the program runs.
