from colorama import Style, Fore
import datetime
import auto_myon
import json
import os


# Probably not a good idea to store usernames and passwords in plain text ~ too lazy to fix
def create_file():
    print(Fore.CYAN+"<<Portal Login>>"+Fore.WHITE)
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
    auto_myon.debug("Checking if creds.json exists")
    if os.path.isfile("./creds.json") == False:
        auto_myon.debug("creds.json file doesn't exist! => Creating file...")
        create_file()
        auto_myon.debug("Reading creds.json")
        CREDENTIALS = read_file()
    else:
        auto_myon.debug("Found creds.json!")
        auto_myon.debug("Reading creds.json")
        print(Fore.GREEN+Style.BRIGHT+"[!] Using Saved Login Details"+Fore.WHITE+Style.NORMAL)
        CREDENTIALS = read_file()
    
    auto_myon.debug("Returning details...")
    return CREDENTIALS