import subprocess
import requests
from tqdm import tqdm
import zipfile
import os
import platform

def extract(file_name):
    # Extract
    with zipfile.ZipFile(file_name, 'r') as zipref:
        if "gecko" in file_name:
            zipref.extractall(r"./web_drivers/geckodriver")
        elif "chrome" in file_name:
            zipref.extractall(r"./web_drivers/chromedriver")
        else:
            zipref.extractall("./drivers/" + file_name)
    
    # Clean up by deleting zip file
    os.remove(file_name)

def downloadFirefox():
    filename = None

    # Download geckodriver
    if platform.architecture()[0] == "64bit":
        url = "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip"
        filename = "geckodriver-v0.26.0-win64.zip"
    else:
        url = "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win32.zip"
        filename = "geckodriver-v0.26.0-win32.zip"

    response = requests.get(url, stream=True)
    file_size = int(response.headers.get('Content-Length'))

    with open(filename, "wb") as handle:
        for data in tqdm(response.iter_content(), total=file_size):
            handle.write(data)

    # Unzip the zip file and extract main geckodriver.exe
    extract(filename)

def downloadChrome():
    filename = None

    if platform.architecture()[0] == "64bit":
        url = ""
        filename = ""
    else:
        url = ""
        filename = ""

    response = requests.get(url, stream=True)
    file_size = int(response.headers.get('Content-Length'))

    with open(filename, 'wb') as handle:
        for data in tqdm(response.iter_content(), total=file_size):
            handle.write(data)

    extract(filename)

def downloadDrivers(browser):
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
            return True
        except Exception as e:
            debug("Error downloading chromedrivers\n" + e)
            return False