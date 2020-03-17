# NOTE: IT IS ADVISED TO NO LONGER USE THIS SOFTWARE
As of 3/17/2020 @ 3 AM, I have looked back into this code and found that this dumpster fire of a codebase is buggy as hell and needs to be refactored and optimized to be flexible in a GUI that might be later implmented in a sucessor project with a different, cooler name compared to this lame name. As far as im concerned, I am archiving and halting this project as a result of this disaster. Hopefully I will return to this project, making it deprecated and create a sucessor to this project with a GUI in order to make the user experience better, cleaner code, contain most of the current features, and implement the TODOS below.
# TODO:
- Handle errors better
	- Like make it friendly when exiting instead of spilling a bunch of errors
- Somehow make ID of some inputs persistent (kind of impossible)
- Reuse already downloaded webdrivers
- Handle credentials better than storing it in a plain json file
# aut0_my0n
Nobody wants to read boring kindergarten books online, that's why this exists.
![Demo Image of auto_myon](https://github.com/Astrol99/aut0_my0n/blob/master/resources/Capture.PNG)
## Installation Guide
#### Supported OS
- Windows
- ~macOS~ Soon...
#### Supported Browsers
- Chrome
- Firefox
### Using pre-built binaries
1. Go to the releases section at https://github.com/Astrol99/aut0_my0n/releases then go to the latest one
2. Download the zip folder named "auto_myon.x.x.x.zip"
3. Extract the folder
4. Go into the folder
5. Click on auto_myon.exe
6. Enjoy!
### Self-Compile
1. Git clone this repo
```
git clone
```
2. Go into the directory then install the required libraries
```
pip3 install -r requirements.txt
```
3. Run the main program
```
python3 auto_myon.py
```
