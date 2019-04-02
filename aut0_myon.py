import pyautogui
import time
import os

#print(pyfiglet.figlet_format("aut0_my0n", font="slant"))

print("""
               __  ____                       ____      
  ____ ___  __/ /_/ __ \     ____ ___  __  __/ __ \____ 
 / __ `/ / / / __/ / / /    / __ `__ \/ / / / / / / __ \\
/ /_/ / /_/ / /_/ /_/ /    / / / / / / /_/ / /_/ / / / /
\__,_/\__,_/\__/\____/____/_/ /_/ /_/\__, /\____/_/ /_/ 
                    /_____/         /____/          
                    
                | Version: 1.0.0 |       
                 | By: Astrol99 | 

TIP: Press Ctrl or Control + C to exit program!\n
""")

tabs = int(input("[i] Amount of tabs open: ")) + 1
timeWait = int(input("[i] Amount of seconds per wait: "))

print("\n[!] Starting in 5 seconds...")

time.sleep(5)

try:
    print("[!] Started! -> Please enjoy your free myon minutes!")
    while True:
        print("[~] Started loop...")
        for i in range(tabs):
            if i == 0:
                continue # Used to pass loop 0
            print(f"\n[*] On tab: {i}...")
            time.sleep(0.5)
            if os.name == "nt":
                pyautogui.hotkey("ctrl", str(i))
            else:
                pyautogui.hotkey("command" , str(i))
            print(f"[+] Switched tabs to tab: {i}")
            pyautogui.press("right")
            print("[+] Pressed right -> Turned page")
        print(f"[*] On cooldown for {timeWait} secs...")
        time.sleep(timeWait)
except KeyboardInterrupt:
    print("[!] Stopped! -> exiting...")
    exit()
