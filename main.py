import hashlib
import time
import config

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def create_user(username, password, user_type):
    with open("users.txt", "r") as user_file:
        for line in user_file:
            data = line.strip().split(",")
            if data[0] == username:
                print("Username already exists.")
                return

    if user_type == "staff":
        staff_verification = input("Enter staff verification code: ")

        if staff_verification != config.STAFF_VERIFICATION_CODE:
            print("Staff verification code is incorrect. Staff registration denied.")
            return

    hashed_password = hash_password(password)
    with open("users.txt", "a") as user_file:
        if user_type == "staff":
            privilege_level = int(input("Enter Privilege Level greater than 5 "))
            privilege_level = 5 if privilege_level < 5 else privilege_level
        else:
            privilege_level = int(input("Enter Privilege Level less than 5 "))
            privilege_level = 4 if privilege_level > 5 else privilege_level
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


def write_data(username, password, data_type, data, sensitivity_level, patient):
    privilege_level = check_credentials(username, password)[1]

    if privilege_level < sensitivity_level:
        print("Insufficient privilege level to write this data.")
        return
    if check_user(patient) == False:
        print("Patient doesn't exist.")
        return

    if sensitivity_level > 10:
        print("Sensitivity level should not be greater than 10.")
        return
    
    timestamp = int(time.time()) 
    formatted_date = time.strftime("%Y/%m/%d", time.gmtime(timestamp))

    with open("data.txt", "a") as data_file:
        data_file.write(f"{patient},{data_type},{data},{sensitivity_level},{formatted_date}\n")
        print("Data written successfully.")


def read_data(username, password, data_type):
    user_type, privilege_level = check_credentials(username, password)
    found_data = False 

    try:
        with open("data.txt", "r") as data_file:
            for line in data_file:
                data = line.strip().split(",")
                sensitivity_level = int(data[3])
                
                if user_type == "patient" and data[0] == username and privilege_level >= sensitivity_level:
                    print(f"Patient: {data[0]} Data-type: {data[1]} Data: {data[2]} Date:{data[4]} Sensitivity Level: {sensitivity_level}")
                    found_data = True  

                elif user_type != "patient" and data[1] == data_type :
                    print(f"Patient: {data[0]} Data-type: {data[1]} Data: {data[2]} Date:{data[4]} Sensitivity Level: {sensitivity_level}")
                    found_data = True  

    except FileNotFoundError:
        print(f"Record of File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    if not found_data:
        print("No data can be provided")



username = None
password = None
user_type = None
privilege_level = 0

while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_type = input("Enter user type (patient or staff): ")
        if user_type not in ["patient", "staff"]:
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
        if user_type == "staff":
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
