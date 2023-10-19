import hashlib
import time
import config
from user_manager import create_user, check_credentials, check_user
from hash_password import hash_password


def write_data(username, password, data_type, data, sensitivity_level, patient):
    privilege_level = check_credentials(username, password)[1]

    if privilege_level < sensitivity_level:
        print("Insufficient privilege level to write this data.")
        return
    if check_user(patient) == False:
        print("Patient doesn't exist.")
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

                elif (user_type == "doctor" or user_type == "staff" )and data[1] == data_type and privilege_level >= sensitivity_level:
                    print(f"Patient: {data[0]} Data-type: {data[1]} Data: {data[2]} Date:{data[4]} Sensitivity Level: {sensitivity_level}")
                    found_data = True  

                elif user_type == "admin" and data[1] == data_type :
                    print(f"Patient: {data[0]} Data-type: {data[1]} Data: {data[2]} Date:{data[4]} Sensitivity Level: {sensitivity_level}")
                    found_data = True

    except FileNotFoundError:
        print(f"Record of File not found.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    if not found_data:
        print("No data can be provided")
