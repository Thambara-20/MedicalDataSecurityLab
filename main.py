import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Function to create a new user account
def create_user(username, password, user_type, privilege_level):
    with open("users.txt", "a") as user_file:
        hashed_password = hash_password(password)
        user_file.write(f"{username},{hashed_password},{user_type},{privilege_level}\n")

def check_credentials(username, password):
    with open("users.txt", "r") as user_file:
        for line in user_file:
            data = line.strip().split(",")
            if data[0] == username and data[1] == hash_password(password):
                return data[2], int(data[3])
    return None, 0
