from selenium import webdriver

phantomJS_PATH = "C:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\phantomjs.exe"
driver = webdriver.PhantomJS(executable_path=phantomJS_PATH)

URL = "https://stackoverflow.com"
BUTTON_PATH = ""

driver.get(URL)
driver.save_screenshot("test.png")
driver.close()