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

create_user("user3", "password", "user", 5)
write_data('user1',"password",'sickness',"data...",2)
read_data('user1',"password",'sickness')
