## Hospital Management Project with-MySQL and Python: 

The Hospital Management System is designed to store and manage essential data related to hospitals, including patient records, doctor details, and appointment scheduling. The system provides users with options to register, log in, and navigate a menu with three main functionalities: Administration, Billing, and Appointment.

## Resources
-  VScode- for python implementation
-  MySQL Workbench

## Functions used

drfetchdata()-     Display the details of doctors 
patfetchdata()-    Display the details of patients  
dradddata()-       To add details of doctors 
patadddata()-      To add details of patients 
drdeldata()-       To delete the details of doctors  
patdeldata()-      To delete the details of patients 
apadddata()-       To add the appointment details   
apupdata()-        To modify the appointment details  
apdeldata()-       To delete the appointment details  
 
## Concepts used

User Authentication:
Registration and Login: The system uses a MySQL database to store user credentials. It allows new users to register by creating a username and password, which are stored securely in the database.

Data Management:
Doctor and Patient Information: Functions like dradddata() and patadddata() allow the addition of new doctor and patient details to the database. The system includes functionalities to fetch, add, delete, and update doctor and patient records using MySQL queries.
Appointment Management: The apadddata(), apupdata(), and apdeldata() functions allow users to manage appointment data, such as booking, modifying, or canceling appointments.

MySQL Database Integration:
The project heavily relies on MySQL for data storage and management, using various SQL queries for data retrieval and manipulation. The connection to the database is established using the MySQL connector in Python, which facilitates interaction with the database for functions like retrieving doctor/patient information or updating appointment schedules.

Menu-Driven Interface:
The system is designed with a menu-driven interface that provides options for administration (viewing, adding, or deleting records), billing (checking payment status and updating records), and appointment scheduling. This interface allows for organized navigation between different sections of the hospital management functionalities.

Modular Function Design:
Functions like drfetchdata(), patfetchdata(), apadddata(), etc., each perform specific tasks, enhancing code modularity and readability. Each function is dedicated to a unique task, like fetching doctor data or adding patient information, making the system organized and easy to maintain.

Date and Time Handling:
The project uses the datetime module to display the current date and time. This can be useful for timestamping appointments or generating billing records.
