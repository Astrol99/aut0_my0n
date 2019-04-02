import pyautogui
import pyfiglet
import time
import os

print(pyfiglet.figlet_format("aut0_my0n", font="slant"))
print("~ A program that reads books for you to increase minutes on MyOn and increased with mutiple tabs")
print("By: David Nguyen\nTIP: press ctrl+c to stop the program when focused on terminal!\n")

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
            pyautogui.press("right")
            print("[+] Pressed right")
            time.sleep(1)
            if os.name == "nt":
                pyautogui.hotkey("ctrl", str(i))
            else:
                pyautogui.hotkey("command" , str(i))
            print("[+] Switched tabs")
        print(f"[*] On cooldown for {timeWait} secs...")
        time.sleep(timeWait)
except KeyboardInterrupt:
    print("[!] Stopped! -> exiting...")
    exit()
