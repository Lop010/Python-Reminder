from tkinter import*
import time
from win10toast import *
from pathlib import Path


root = Tk()
root.title("Windows Reminder Tool")
root.geometry("700x200")
root.resizable(False, False)
# Get Script Directory

script_dir = Path(__file__).parent.absolute()
print(script_dir)

# Display entryfield1 and "entry name1"
Label(text=("What Should The Notification Say?"),
      font="none 10 bold", ) .grid(row=0, column=1, sticky=W)

textentry1 = Entry(root, width=37, font=("none 8 bold"))
textentry1.grid(row=1, column=1, sticky=W)


# Display entryfield1 and "entry name1"
Label(text=("How Long Until You Want To Get Notified (Choose below if you want hours, days, minutes or seconds)"),
      font="none 10 bold") .grid(row=2, column=1, sticky=W)

textentry2 = Entry(root, width=37, font=("none 8 bold"))
textentry2.grid(row=3, column=1, sticky=W)

# Choose hours, minutes or days
Label(text=("Do you want hours, days, minutes or seconds (Type in what you want)"),
      font="none 10 bold") .grid(row=4, column=1, sticky=W)

mhd = Entry(root, width=37, font=("none 8 bold"))
mhd.grid(row=5, column=1, sticky=W)


# Take input from use and turn it into seconds (time.sleep uses seconds)


# Function

def popupmsgtimer():
    notifyinfo = (textentry1.get())
    howlongwait = (textentry2.get())
    hmhd = (mhd.get())
    global formula
    
    if hmhd == ("minutes"):
        formula = 60

    elif hmhd == ("hours"):
        formula = 3600

    elif hmhd == ("days"):
        formula = 86400

    elif hmhd == ("seconds"):
        formula = 1


    number1 = float(formula)
    number2 = float(howlongwait)

    resualt = (number1 * number2)
    
    sualt = int(resualt)
    time.sleep(sualt)
    toaster = ToastNotifier()
    toaster.show_toast("WinReminder", (notifyinfo), duration=10, threaded=True)


def test():

    notifyinfo = (textentry1.get())
    howlongwait = (textentry2.get())
    hmhd = (mhd.get())
    notifyinfo = (textentry1.get())
    howlongwait = (textentry2.get())
    hmhd = (mhd.get())
    
    if hmhd == ("minutes"):
        formula = 60

    elif hmhd == ("hours"):
        formula = 3600

    elif hmhd == ("days"):
        formula = 86400

    elif hmhd == ("seconds"):
        formula = 1


    number1 = float(formula)
    number2 = float(howlongwait)

    resualt = (number1 * number2)
    
    sualt = int(resualt)
    print(sualt)
    print(notifyinfo)
    print(hmhd)
    


Button(root, text="Scheduale Notification", width=22,
       command=(popupmsgtimer)) .grid(row=8, column=1, sticky=W)

Button(root, text="Test", width=22,
       command=(test)) .grid(row=7, column=1, sticky=W)

root.mainloop()
