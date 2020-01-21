from selenium import webdriver
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
    if os.path.isfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"):
        print(Fore.GREEN+Style.BRIGHT+"--- Found chrome! => Using chrome as primary browser ---"+Fore.WHITE+Style.NORMAL)
        return "chrome"
    else:
        auto_myon.debug("Found no browser!")
        return None

# Decides which driver to use
def getDriver(browser=check()):
    if browser == "firefox":
        driver = webdriver.Firefox(executable_path=os.path.abspath("./web_drivers/geckodriver.exe"))
    elif browser == "chrome":
        driver = webdriver.Chrome(executable_path=os.path.abspath("./web_drivers/chromedriver.exe"))
    else:
        print("[-] Invalid Browser Type! Exiting...")
        exit()

    return driver