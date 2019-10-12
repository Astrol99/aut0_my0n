from selenium import webdriver
import datetime
import time
import os

PORTAL = "https://my.harmonytx.org"

def debug(debug_info):
    now = datetime.datetime.now()
    debug_time = f"{now.hour}:{now.minute}:{now.second}"
    print(f"[DEBUG {debug_time}] {debug_info}")

def driver_path(browser):
    if browser == "firefox":
        driver = webdriver.Firefox(executable_path=os.path.abspath("./web_drivers/geckodriver.exe"))
    elif browser == "chrome":
        driver = webdriver.Chrome(executable_path=os.path.abspath("./web_drivers/chromedriver.exe"))
    else:
        print("[-] Invalid Browser Type! Exiting...")
        exit()

    return driver

def aut0_myon():
    browser = input(f"[!] Firefox or Chrome?: ").lower()
    driver = driver_path(browser)

    debug("Logging into portal...")
    driver.get(PORTAL)
    time.sleep(3)

    driver.close()

if __name__ == '__main__':
    aut0_myon()