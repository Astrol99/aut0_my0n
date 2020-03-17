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
        for data in tqdm(response.iter_content(), total=file_size, ascii=True):
            handle.write(data)

    # Unzip the zip file and extract main geckodriver.exe
    extract(filename)

def downloadChrome():
    def getLatestChromeVersion():
        url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
        response = requests.get(url)
        
        return response.text

    filename = "chromedriver_win32.zip"
    latestVersion = getLatestChromeVersion()

    url = f"https://chromedriver.storage.googleapis.com/{latestVersion}/chromedriver_win32.zip"

    response = requests.get(url, stream=True)
    file_size = int(response.headers.get('Content-Length'))

    with open(filename, 'wb') as handle:
        for data in tqdm(response.iter_content(), total=file_size, ascii=True):
            handle.write(data)

    extract(filename)

# Should probably use already downloaded drivers instead of downloading new ones again and again, wasting gigabytes of downloads
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