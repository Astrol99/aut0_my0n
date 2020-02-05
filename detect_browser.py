from selenium import webdriver
from colorama import Style, Fore
import auto_myon
import os

# C:\Program Files\Mozilla Firefox\firefox.exe
# C:\Program Files (x86)\Google\Chrome\Application\chrome.exe

def checkBrowser():
    auto_myon.debug("Checking if firefox or chrome is installed...")
    if os.path.isfile(r"C:\Program Files\Mozilla Firefox\firefox.exe"):
        print(Fore.GREEN+Style.BRIGHT+"--- Found firefox! => Using firefox as primary browser ---"+Fore.WHITE+Style.NORMAL)
        return "firefox"
    if os.path.isfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"):
        print(Fore.GREEN+Style.BRIGHT+"--- Found chrome! => Using chrome as primary browser ---"+Fore.WHITE+Style.NORMAL)
        return "chrome"
    else:
        print(Fore.RED+Style.BRIGHT+"[-] Unable to find compatible browsers... Please install firefox or google chrome. Or move the installation into the default directory."+Fore.WHITE+Style.NORMAL)
        exit(1)

# Decides which driver to use
def getDriver(browser):
    if browser == "firefox":
        driver = webdriver.Firefox(executable_path=os.path.abspath("./web_drivers/geckodriver/geckodriver.exe"))
    elif browser == "chrome":
        driver = webdriver.Chrome(executable_path=os.path.abspath("./web_drivers/chromedriver/chromedriver.exe"))
    else:
        print("[-] Invalid Browser Type! Exiting...")
        exit()

    return driver