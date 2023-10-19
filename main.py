import hashlib
import time
import config
from user_manager import create_user, check_credentials, check_user
from hash_password import hash_password
from file_manager import write_data, read_data



username = None
password = None
user_type = None
privilege_level = 0

print("\n Welcome to the Hospital Management System.")
print("1. Create a new user | 2. Login | 3. Write data | 4. Read data | 5. Exit program \n")


while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_type = input("Enter user type (patient/staff/doctor): ")
        if user_type not in ["patient", "admin","doctor","staff"]:
            print("Invalid user type. Please choose 'patient' or 'staff'.")
        else:
            create_user(username, password, user_type)


    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_type, privilege_level = check_credentials(username, password)
        if user_type:
            print(f"Login successful. User type: {user_type}, Privilege Level: {privilege_level}")
        else:
            print("Invalid credentials.")

    elif choice == "3":
        if  user_type in ["admin","doctor","staff"]:
            patient = input("Enter patient name: ")
            data_type = input("Enter data type (personal, sickness, drug, lab): ")
            data = input("Enter data: ")
            sensitivity_level = int(input("Enter sensitivity level:0 to 10 "))
            write_data(username, password, data_type, data, sensitivity_level, patient)
        else:
            print("A staff member should be logged in.")

    elif choice == "4":
        data_type = input("Enter data type (personal, sickness, drug, lab): ")
        read_data(username, password, data_type)

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
