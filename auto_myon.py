from selenium import webdriver
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

    # Main browsing functions 
    def read(self):
        # Goes to harmony portal to log in through clever then myon
        debug("Going into portal...")
        self.driver.get(self.PORTAL)

        self.login()

if __name__ == '__main__':
    BROWSER = input(f"[!] Firefox or Chrome?: ").lower()
    USERNAME = input(f"[!] Username: ")
    PASSWORD = input(f"[!] Password: ")

    myon = auto_myon(BROWSER, USERNAME, PASSWORD)
    myon.read()