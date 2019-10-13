import datetime
from auto_myon import debug
import json
import os

def create_file():
    USERNAME = input(f"[!] User ID: ")
    PASSWORD = input(f"[!] Password: ")

    cred_dict = {"username": USERNAME,"password": PASSWORD}

    with open("creds.json", "w") as json_file:
        json.dump(cred_dict, json_file, indent=4)
        json_file.close()

def read_file():
    with open("./creds.json") as json_file:
        data = json.load(json_file)
        json_file.close()

    USERNAME = data["username"]
    PASSWORD = data["password"]
    CREDENTIALS = USERNAME, PASSWORD
    
    return CREDENTIALS 

def get():
    debug("Checking if creds.json exists")
    if os.path.isfile("./creds.json") == False:
        debug("creds.json file doesn't exist! => Creating file...")
        create_file()
        debug("Reading creds.json")
        CREDENTIALS = read_file()
    else:
        debug("Found creds.json!")
        debug("Reading creds.json")
        CREDENTIALS = read_file()
    
    debug("Returning details...")
    return CREDENTIALS