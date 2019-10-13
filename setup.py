from cx_Freeze import setup, Executable

base = None    

executables = [Executable("auto_myon.py", base=base)]

packages = ["idna", "selenium", "pyfiglet", "colorama"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "auto_myon",
    options = options,
    version = "2.2.1",
    description = 'A program that gives you minutes on myon',
    executables = executables
)