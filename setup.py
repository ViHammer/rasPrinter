from cx_Freeze import setup, Executable

base = None    

executables = [Executable("installer.py", base=base)]

packages = ["winreg", "pathlib", "urllib.request", "tkinter", "subprocess", "os"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "rasPrint installer",
    options = options,
    version = "0",
    description = 'installs rasPrinter',
    executables = executables
)
