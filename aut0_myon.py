from selenium import webdriver

PORTAL = "https://my.harmonytx.org"

browser = input("Firefox or Chrome?: ")

if browser == "Firefox":
    driver = webdriver.Firefox()
elif browser == "Chrome":
    driver = webdriver.Chrome()
else:
    print("Invalid choice")
    exit()

driver.close()