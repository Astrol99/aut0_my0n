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
        # Username part
        debug("Finding username input box")
        username_box = self.driver.find_element_by_id("identification")
        debug("Entering login credentials")
        username_box.send_keys(USERNAME)
        debug("Submitting username...")
        username_submit_btn = self.driver.find_element_by_id("authn-go-button")
        username_submit_btn.click()

        # Password part


    def read(self):
        debug("Opening browser...")
        self.driver = self.driver_path(BROWSER)

        # Goes to harmony portal to log in through clever then myon
        debug("Going into portal...")
        self.driver.get(self.PORTAL)

        self.login()

        time.sleep(10)

        self.driver.close()

if __name__ == '__main__':
    BROWSER = input(f"[!] Firefox or Chrome?: ").lower()
    USERNAME = input(f"[!] Username: ")
    PASSWORD = input(f"[!] Password: ")

    myon = auto_myon(BROWSER, USERNAME, PASSWORD)
    myon.read()