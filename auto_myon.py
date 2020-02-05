from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore, Back, Style
import detect_browser
import credentials
import pyfiglet
import datetime
import time
import sys
import os
import drivers

init() # Initalizes colorama lib

# Gives time info on what program is doing for debug purposes
def debug(debug_info):
    if "-v" in sys.argv:
        now = datetime.datetime.now()
        debug_time = f"{now.hour}:{now.minute}:{now.second}"
        print(Style.BRIGHT+Fore.YELLOW+f"[DEBUG {debug_time}] {debug_info}"+Style.NORMAL+Fore.WHITE)
    else:
        pass

class auto_myon:
    def __init__(self):
        self.PORTAL = "https://my.harmonytx.org"
        self.USERNAME , self.PASSWORD = credentials.get()
        self.BROWSER = detect_browser.checkBrowser()

        # Get webdriver
        # Download drivers from website and save it into drivers dir
        print(Fore.CYAN+Style.BRIGHT+"[*] Downloading webdriver..."+Fore.WHITE+Style.NORMAL)
        downloadStatus = drivers.downloadDrivers(self.BROWSER)

        if downloadStatus == False:
            print("Error downloading webdrivers")
            exit()

        # Set browser parameters
        print(Fore.CYAN+Style.BRIGHT+"[*] Opening browser and redirecting to portal..."+Fore.WHITE+Style.NORMAL)
        self.driver = detect_browser.getDriver(self.BROWSER)    # Open drivers according to self.BROWSER
        self.driver.set_window_size(1000,800)

    def login(self):
        # Submit info element
        #submit_btn = self.driver.find_element_by_id("authn-go-button")
        submit_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "authn-go-button")))

        # Username part
        debug("Finding username input box")
        username_box = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "identification")))
        #username_box = self.driver.find_element_by_id("identification")
        debug("Entering username credentials")
        username_box.send_keys(self.USERNAME)
        debug("Submitting username...")
        submit_btn.click()

        # Password part
        debug("Finding password input box...")
        try:
            password_box = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "ember516")))
            #password_box = self.driver.find_element_by_id("ember516")
        except Exception as e:
            debug(f"ELEMENT ERROR: UNABLE TO FIND ELEMENT\n{e}")
            self.driver.quit()
            exit()
        debug("Entering password credentials")
        password_box.send_keys(self.PASSWORD)
        debug("Submitting password...")
        submit_btn.click()
    
    def jump_tabs(self):
        # Opens clever tab
        debug("Opening new tab")
        self.driver.execute_script("window.open('');")
        debug("Switching to clever window")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://clever.com/in/hps/student/portal?skip=1&specify_auth=saml")

        time.sleep(3)

        # Opens myon tab
        debug("Opening new tab")
        self.driver.execute_script("window.open('');")
        debug("Switching to myon window")
        self.driver.switch_to.window(self.driver.window_handles[2])
        myon_link = "https://clever.com/oauth/authorize?channel=clever-portal&client_id=e9883f835c1c58894763&confirmed=true&district_id=53fbb405cfc2cc490d000006&redirect_uri=https%3A%2F%2Fwww.myon.com%2Fapi%2Foauth%2Fsso.html%3Ainstantlogin&response_type=code"
        self.driver.get(myon_link)

    def myon_nav(self):
        print(Fore.CYAN+"<<Options>>"+Fore.WHITE)
        mins = int(input("[!] Read Time? (minutes): "))
        delay = int(input("[!] Delay per page? (seconds): "))
        input("[!] Please select one book then press enter to start reading ")

        endTime = datetime.datetime.now() + datetime.timedelta(minutes=mins)
        print(Fore.GREEN+Style.BRIGHT+"--> Estimated to be complete in "+str(endTime)+Fore.WHITE+Style.NORMAL)

        debug("Finding next page button")
        right_btn = self.driver.find_element_by_class_name("stage_button.-rightArrow")
        debug("Initating read function...")
        debug("Running loop...")

        print("\n~ auto_myon is now running in the background - Press CTRL + C to exit ~")
        
        while datetime.datetime.now() <= endTime:
            try:
                right_btn.click()
                time.sleep(delay)
            except KeyboardInterrupt:
                debug("User interrupted; exiting...")
                break

    # Main browsing functions 
    def read(self):
        try:
            # Goes to harmony portal to log in through clever then myon
            debug("Going into portal...")
            self.driver.get(self.PORTAL)

            self.login()
            self.jump_tabs()
            self.myon_nav()
        except Exception as e:
            debug(f"ERROR: {e}")
        print("[+] Finished reading! You may now close the browser window")
        self.driver.quit()
        input("\nPress enter to quit...")

if __name__ == '__main__':
    print(Fore.CYAN+"-"*60)
    print(Fore.RED+pyfiglet.figlet_format("auto_myon", "slant"))
    print(Fore.CYAN+"-"*60+Fore.WHITE)
    print(Fore.YELLOW+"> v3.0.0")
    print(Fore.YELLOW+"> Made by: astrol99\n"+Fore.WHITE)
    
    myon = auto_myon()
    myon.read()