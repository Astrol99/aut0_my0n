import auto_myon
import os

# C:\Program Files\Mozilla Firefox\firefox.exe
# C:\Program Files (x86)\Google\Chrome\Application\chrome.exe

def check():
    auto_myon.debug("Checking if firefox or chrome is installed...")
    if os.path.isfile(r"C:\Program Files\Mozilla Firefox\firefox.exe"):
        print("--- Found firefox! => Using firefox as primary browser ---")
        return "firefox"
    elif os.path.isfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"):
        print("--- Found chrome! => Using chrome as primary browser ---")
        return "chrome"
    else:
        auto_myon.debug("Found no browser!")
        return None