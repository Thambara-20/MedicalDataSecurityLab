
import time
import config
from hash_password import hash_password


def create_user(username, password, user_type):
    with open("users.txt", "r") as user_file:
        for line in user_file:
            data = line.strip().split(",")
            if data[0] == username:
                print("Username already exists.")
                return

    privilege_level = 0  # Default privilege level
    verification_code = None

    if user_type == "admin":
        privilege_level = config.ADMIN_PRIVILEGE_LEVEL
        verification_code = config.ADMIN_VERIFICATION_CODE
    elif user_type == "doctor":
        privilege_level = config.DOCTOR_PRIVILEGE_LEVEL
        verification_code = config.DOCTOR_VERIFICATION_CODE
    elif user_type == "staff":
        privilege_level = config.STAFF_PRIVILEGE_LEVEL
        verification_code = config.STAFF_VERIFICATION_CODE
    else:
        privilege_level = config.PATIENT_PRIVILEGE_LEVEL

    if user_type in ["admin", "doctor", "staff"]:
        staff_verification = input(f"Enter {user_type} verification code: ")

        if staff_verification != verification_code:
            print(f"{user_type} verification code is incorrect. {user_type} registration denied.")
            return
        
    hashed_password = hash_password(password)
    with open("users.txt", "a") as user_file:

        user_file.write(f"{username},{hashed_password},{user_type},{privilege_level}\n")
        print(f"User Signup Successful.. [ username: {username}  privilege_level: {privilege_level} ]")

def check_credentials(username, password):
    with open("users.txt", "r") as user_file:
        for line in user_file:
            data = line.strip().split(",")
            if data[0] == username and data[1] == hash_password(password):
                return data[2], int(data[3])
    return None, 0


def check_user(user_name):
    with open("users.txt", "r") as user_file:
        for line in user_file:
            data = line.strip().split(",")
            if data[0] == user_name:
                return True
    return False
