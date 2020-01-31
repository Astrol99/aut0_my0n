import subprocess
import requests
from tqdm import tqdm

# C:\Program Files\Mozilla Firefox\firefox.exe
# C:\Program Files (x86)\Google\Chrome\Application\chrome.exe

"""
def getBrowserVersion(browser):
    if browser is "firefox":
        # Geckodriver v0.26.0 minimum recommended Firefox version: >= 60
        version = subprocess.check_output("C:\\Program Files\\Mozilla Firefox\\firefox.exe -v | more".split()).decode("utf-8")
        version = version.replace("\r\n", "")[16:]  # Get only version num and clean up string
        
        if int(version.split(".")[0]) < 60:   # Get first number seperated by "." Ex: 72.0.1 and test if it's less than 60
            return None

        print("Got firefox version: " + version)

    elif browser is "chrome":
        url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
        response = requests.request("GET", url)
        version = response.text

    return version
"""

def extract(file_name):
    pass

def downloadFirefox():
    # Download geckodriver
    url = "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win32.zip"
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get('Content-Length'))

    with open("geckodriver-v0.26.0-win32.zip", "wb") as handle:
        for data in tqdm(response.iter_content(), total=file_size):
            handle.write(data)

    # Unzip the zip file and extract main geckodriver.exe
    extract("geckodriver-v0.26.0-win32.zip")

    # Make new folder: "drivers"

    # Move geckodriver into that folder


def downloadChrome():
    pass

def downloadDrivers(browser):
    # version = getBrowserVersion(browser)

    if browser is "firefox":
        try:
            downloadFirefox()
            return True
        except Exception as e:
            debug("Error download geckodriver...\n" + e)
            return False

    elif browser is "chrome":
        try:
            downloadChrome()
            
        except Exception as e:
            debug("Error downloading chromedrivers\n" + e)

downloadFirefox()