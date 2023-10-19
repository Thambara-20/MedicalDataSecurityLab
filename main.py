import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def create_user(username, password, user_type, privilege_level):
    hashed_password = hash_password(password)
    with open("users.txt", "r") as user_file:
        for line in user_file:
            data = line.strip().split(",")
            if data[0] == username:
                print("Username already exists.")
                return 
    with open("users.txt", "a") as user_file:
        user_file.write(f"{username},{hashed_password},{user_type},{privilege_level}\n")

def check_credentials(username, password):
    with open("users.txt", "r") as user_file:
        for line in user_file:
            data = line.strip().split(",")
            if data[0] == username and data[1] == hash_password(password):
                return data[2], int(data[3])
    return None, 0

def write_data(username, password, data_type, data, sensitivity_level):
    privilege_level = check_credentials(username, password)[1]

    if privilege_level < sensitivity_level:
        print("Insufficient privilege level to write this data.")
        return

    with open(f"{data_type}.txt", "a") as data_file:
        data_file.write(f"{username},{data},{sensitivity_level}\n")
        print("Data written successfully.")

def read_data(username, password, data_type):
    privilege_level = check_credentials(username, password)[1]

    with open(f"{data_type}.txt", "r") as data_file:
        for line in data_file:
            data = line.strip().split(",")
            sensitivity_level = int(data[2])
            if privilege_level >= sensitivity_level:
                print(f"Data: {data[1]}, Sensitivity Level: {sensitivity_level}")


username = None
password = None
user_type = None
privilege_level = 0

while True:
    choice = input("Enter your choice: ")

    if choice == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_type = input("Enter user type (patient or staff): ")
        privilege_level = int(input("Enter privilege level: "))
        create_user(username, password, user_type, privilege_level)
        print("User created successfully.")

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
            print("dddddddddddddd")
            data_type = input("Enter data type (personal, sickness, drug, lab): ")
            data = input("Enter data: ")
            sensitivity_level = int(input("Enter sensitivity level: "))
            write_data(username, data_type, data, sensitivity_level)
        else:
            print("Patients cannot write data.")

    elif choice == "4":
        data_type = input("Enter data type (personal, sickness, drug, lab): ")
        read_data(username, data_type)

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")