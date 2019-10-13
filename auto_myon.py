from selenium import webdriver
import credentials
import pyfiglet
import datetime
import time
import os

# Gives time info on what program is doing for debug purposes
def debug(debug_info):
    now = datetime.datetime.now()
    debug_time = f"{now.hour}:{now.minute}:{now.second}"
    print(f"[DEBUG {debug_time}] {debug_info}")

class auto_myon:
    def __init__(self, browser, username, password):
        self.PORTAL = "https://my.harmonytx.org"
        self.BROWSER = browser
        self.USERNAME = username
        self.PASSWORD = password

        debug("Opening browser...")
        self.driver = self.driver_path(BROWSER)
        self.driver.set_window_size(1000,800)

    # Decides which driver to use
    def driver_path(self, browser):
        if browser == "firefox":
            driver = webdriver.Firefox(executable_path=os.path.abspath("./web_drivers/geckodriver.exe"))
        elif browser == "chrome":
            driver = webdriver.Chrome(executable_path=os.path.abspath("./web_drivers/chromedriver.exe"))
        else:
            print("[-] Invalid Browser Type! Exiting...")
            exit()

        return driver

    def login(self):
        # Submit info element
        submit_btn = self.driver.find_element_by_id("authn-go-button")

        # Username part
        debug("Finding username input box")
        username_box = self.driver.find_element_by_id("identification")
        debug("Entering username credentials")
        username_box.send_keys(USERNAME)
        debug("Submitting username...")
        submit_btn.click()

        # Password part
        debug("Finding password input box")
        try:
            password_box = self.driver.find_element_by_id("ember516")
        except Exception as e:
            debug(f"ELEMENT ERROR: UNABLE TO FIND ELEMENT\n{e}")
            self.driver.quit()
            exit()
        debug("Entering password credentials")
        password_box.send_keys(PASSWORD)
        debug("Submitting password...")
        submit_btn.click()
    
    def jump_tabs(self):
        # Opens clever tab
        debug("Opening new tab")
        self.driver.execute_script("window.open('');")
        debug("Switching to clever window")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://clever.com/in/hps/student/portal?skip=1&specify_auth=saml")

        time.sleep(2)

        # Opens myon tab
        debug("Opening new tab")
        self.driver.execute_script("window.open('');")
        debug("Switching to myon window")
        self.driver.switch_to.window(self.driver.window_handles[2])
        myon_link = "https://clever.com/oauth/authorize?channel=clever-portal&client_id=e9883f835c1c58894763&confirmed=true&district_id=53fbb405cfc2cc490d000006&redirect_uri=https%3A%2F%2Fwww.myon.com%2Fapi%2Foauth%2Fsso.html%3Ainstantlogin&response_type=code"
        self.driver.get(myon_link)

    def myon_nav(self):
        mins = int(input("[!] Read Time? (minutes): "))
        delay = int(input("[!] Delay per page? (seconds): "))
        input("[!] Please select one book then press enter to start reading ")

        endTime = datetime.datetime.now() + datetime.timedelta(minutes=mins)
        print("--> Estimated to be complete in "+str(endTime))

        debug("Finding next page button")
        right_btn = self.driver.find_element_by_class_name("stage_button.-rightArrow")
        debug("Initating read function...")
        debug("Running loop...")

        print("\n~ auto_myon is now running in the background...you may now enjoy free minutes while doing other tasks ~")
        
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
        print("[!] You may now close the browser window")
        self.driver.quit()

if __name__ == '__main__':
    print("-"*60)
    print(pyfiglet.figlet_format("auto_myon", "slant"))
    print("-"*60)
    print("> v2.1.0 Beta")
    print("> Made by: astrol99")
    BROWSER = input(f"\n[!] Are you using Firefox or Chrome?: ").lower()
    USERNAME, PASSWORD = credentials.get()

    myon = auto_myon(BROWSER, USERNAME, PASSWORD)
    myon.read()