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
A. Patient Management:
- Register new patients
- Search patients by ID or name
- View all registered patients
- Automatic patient ID generation (e.g., P001)

B. Doctor Management:
- Load doctors from CSV file
- Search doctors by:
   - Doctor ID
   - Name
   - Specialty
- Display all doctors with availability days and working hours

C. Appointment Management
- Book appointments with:
     - Conflict checking
     - Doctor availability validation
- Cancel appointments
- Reschedule existing appointments
- Search appointments by patient or doctor
- View all appointments
- Automatic appointment ID generation (e.g., A001)

How to Run the Program: 
- First of all, make sure you have Python 3 installed
- Open the project folder in a terminal or IDE
- Run the file:
  python ClinicManager_Summative_Group_B.py
- Use the menu options to interact with the system

Main Menu Options
1. Add Patient
2. Search Patient
3. Show All Patients
4. Show All Doctors
5. Search Doctor
6. Book Appointment
7. Cancel Appointment
8. Reschedule Appointment
9. Show All Appointments
10. Search Appointments
0. Exit

Error Handling:
The system includes basic error handling using:
- try-except ValueError for invalid numeric input
- try-except Exception for unexpected errors
- Validation checks for:
      - Empty inputs
      - Invalid dates and times
      - Double booking

Learning Outcomes:
This project demonstrates:
- Object-Oriented Programming design
- Real-world problem modeling
- File-based data persistence
- Clean and readable Python code

Conclusion
The Clinic Appointment & Patient Management System successfully remains understandable and functional for our summative project.










These files are automatically created or updated when the program runs.
