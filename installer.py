import winreg as wreg
from pathlib import Path
import urllib.request
import tkinter
from tkinter import *
import subprocess
from tkinter import filedialog
import os

filepath = "C:\\Program Files\\"

def browse_button():
    filepath = filedialog.askdirectory()
    lbl_location.config(text="Program will be installed in " + filepath)

def install(filepath):
    key = wreg.CreateKey(wreg.HKEY_CLASSES_ROOT, r"*\shell\rasPrinter")
    wreg.SetValue(key, 'command', wreg.REG_SZ, filepath + "rasPrinter\\rasPrint.exe\" \"%1\"")
    wreg.SetValueEx(key, 'Icon', 0, wreg.REG_SZ, filepath + "rasPrinter\\rasPrint.exe")
    wreg.SetValueEx(key, '', 0, wreg.REG_SZ, 'rasPrint it')
    key.Close()

    ip = e1.get()
    user = e2.get()
    password = e3.get()
    os.mkdir(filepath + 'rasPrinter')
    url = "https://github.com/ViHammer/rasPrinter/blob/master/build/exe.win-amd64-3.9/print.exe"
    filename, headers = urllib.request.urlretrieve(url, filename=filepath + "rasPrinter\\rasPrint.exe")
    config = open(filepath + "rasPrinter\\" + "config.ini", "w")
    config.write(f"[credentials]\nuser={user}\npassword={password}\nip={ip}\n")
    config.close()


window = Tk()

window.title("rasPrinter Installer")

window.geometry('350x200')

#window.attributes("-fullscreen", True) 
#window.wm_attributes("-topmost", 1)
#window.bind("<Escape>", lambda event:window.destroy())



    #bashCommand = "ls /.../folder/* | xargs egrep ... | xargs lp"
    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #output, error = process.communicate

lbl_ip = Label(window, text="ip")
lbl_user = Label(window, text="user")
lbl_password = Label(window, text="password")
lbl_check = Label(window, text="")
lbl_location = Label(window, text="Program will be installed in " + filepath)

button2 = Button(text="Browse", command= lambda : browse_button)
button2.grid(column=0, row=4)

install_btn = Button(text="Install", command= lambda : install(filepath))
install_btn.grid(column=0, row=5)


lbl_ip.grid(column=0, row=0)
lbl_user.grid(column=0, row=1)
lbl_password.grid(column=0, row=2)
lbl_location.grid(column=0, row=3)


e1 = tkinter.Entry(window, width=10)
e2 = tkinter.Entry(window, width=10)
e3 = tkinter.Entry(window, width=10)


e1.grid(column=1, row=0)
e2.grid(column=1, row=1)
e3.grid(column=1, row=2)


window.mainloop()
