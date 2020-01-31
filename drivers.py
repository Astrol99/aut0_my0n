import subprocess
import requests
from tqdm import tqdm
import zipfile
import os

def extract(file_name):
    # Extract
    with zipfile.ZipFile(file_name, 'r') as zipref:
        if "gecko" in file_name:
            zipref.extractall("./web_drivers/geckodriver.exe")
        elif "chrome" in file_name:
            zipref.extractall("./web_drivers/chromedriver.exe")
        else:
            zipref.extractall("./drivers/" + file_name)
    
    # Clean up by deleting zip file
    os.remove(file_name)

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


def downloadChrome():
    pass

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
            
        except Exception as e:
            debug("Error downloading chromedrivers\n" + e)