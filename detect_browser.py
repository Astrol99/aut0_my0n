from colorama import Style, Fore
import auto_myon
import os

# C:\Program Files\Mozilla Firefox\firefox.exe
# C:\Program Files (x86)\Google\Chrome\Application\chrome.exe

def check():
    auto_myon.debug("Checking if firefox or chrome is installed...")
    if os.path.isfile(r"C:\Program Files\Mozilla Firefox\firefox.exe"):
        print(Fore.GREEN+Style.BRIGHT+"--- Found firefox! => Using firefox as primary browser ---"+Fore.WHITE+Style.NORMAL)
        return "firefox"
    elif os.path.isfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"):
        print(Fore.GREEN+Style.BRIGHT+"--- Found chrome! => Using chrome as primary browser ---"+Fore.WHITE+Style.NORMAL)
        return "chrome"
    else:
        auto_myon.debug("Found no browser!")
        return None