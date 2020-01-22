import subprocess

# C:\Program Files\Mozilla Firefox\firefox.exe
# C:\Program Files (x86)\Google\Chrome\Application\chrome.exe

def getBrowserVersion(browser):
    if browser is "firefox":
        # Geckodriver v0.26.0 minimum recommended Firefox version: >= 60
        version = subprocess.check_output("C:\\Program Files\\Mozilla Firefox\\firefox.exe -v | more".split()).decode("utf-8")
        version = version.replace("\r\n", "")[16:]  # Get only version num and clean up string
        
        if int(version.split(".")[0]) < 60:   # Get first number seperated by "." Ex: 72.0.1 and test if it's less than 60
            return None

    elif browser is "chrome":
        pass
    return version

def downloadDrivers():
    pass

print(getBrowserVersion("firefox"))