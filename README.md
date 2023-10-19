# MedicalDataSecurityLab

This Python program is designed for the secure processing of medical data. It allows for the creation of user accounts, management of privilege levels, and storage and retrieval of sensitive medical data records.

## Features

- **User Account Management:** Create user accounts with usernames, MD5-hashed passwords, user type (patient or hospital staff), and privilege levels.
- **Data Records:** Write and read data records associated with patient encounters, categorized as personal details, sickness details, drug prescriptions, and lab test prescriptions, each with a sensitivity level.
- **Access Control:** Hospital staff can read or write data records based on their privilege levels and the data's sensitivity levels, ensuring data security and privacy compliance.

## Configuration and Data Storage

- User account information is stored in a configuration file, including user details.
- Data records are stored in separate files based on their types, each with associated sensitivity levels for access control.
