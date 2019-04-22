import time
import os
try:
    import pyautogui
except ImportError:
    print("[!] Looks like you don't have pyautogui installed!")
    user_input = input("[/] Would you like to install it now?[Y/n]: ")
    user_input = str(user_input).lower()
    if user_input == "y":
        print("[!] Installing pyautogui...\n")
        if os.name == "nt":
            os.system("pip3 install pyautogui")
        elif os.name == "posix":
            os.system("python3 -m pip install pyautogui")
        print("\n[!] Successfully installed pyautogui -> please run this program again. Exiting...")
        exit()
    elif user_input == "n":
        print("[!] Exiting...")
        exit()
    else:
        print("""[!] Invalid response: Enter either 'y' or 'n' (doesn't matter if it's lowercase or uppercase)      
    -> please run the program again. Exiting...
            """)
        exit()

print("""
               __  ____                       ____      
  ____ ___  __/ /_/ __ \     ____ ___  __  __/ __ \____ 
 / __ `/ / / / __/ / / /    / __ `__ \/ / / / / / / __ \\
/ /_/ / /_/ / /_/ /_/ /    / / / / / / /_/ / /_/ / / / /
\__,_/\__,_/\__/\____/____/_/ /_/ /_/\__, /\____/_/ /_/ 
                    /_____/         /____/          
                    
                | Version: 1.0.1 |       
                 | By: Astrol99 | 

TIP: Press Ctrl or Control + C to exit program!\n
""")

tabs = int(input("[i] Amount of tabs open: ")) + 1
timeWait = int(input("[i] Amount of seconds per wait: "))
verbose = str(input("[i] Turn on verbose?(Sends info about when clicked and etc.)[Y or N]: ")).upper()

print("\n[!] Starting in 5 seconds...")

time.sleep(5)

try:
    print("[!] Started! -> Please enjoy your free myon minutes!")
    while True:
        print("[~] Started loop...")
        for i in range(tabs):
            if i == 0:
                continue # Used to pass loop 0
            if verbose == "Y":
                print(f"\n[*] On tab: {i}...")
            time.sleep(0.5)
            if os.name == "nt":
                pyautogui.hotkey("ctrl", str(i))
            else:
                pyautogui.hotkey("command" , str(i))
            if verbose == "Y":
                print(f"[+] Switched tabs to tab: {i}")
            pyautogui.press("right")
            if verbose == "Y":
                print("[+] Pressed right -> Turned page")
        if verbose == "Y":
            print(f"[*] On cooldown for {timeWait} secs...")
        time.sleep(timeWait)
except KeyboardInterrupt:
    print("[!] Stopped! -> exiting...")
    exit()
