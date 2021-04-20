from cx_Freeze import setup, Executable

base = None    

executables = [Executable("print.py", base=base)]

packages = ["paramiko", "scp", "sys", "configparser"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "rasPrint",
    options = options,
    version = "0",
    description = 'prints on pi',
    executables = executables
)
