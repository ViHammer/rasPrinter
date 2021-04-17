from cx_Freeze import setup, Executable

base = None    

executables = [Executable("print.py", base=base)]

packages = ["idna", "paramiko", "scp"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<printy>",
    options = options,
    version = "0",
    description = ' ',
    executables = executables
)