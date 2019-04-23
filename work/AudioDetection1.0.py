
import winsound
import ctypes
gun1 = winsound.PlaySound('9_mm_gunshot-mike-koenig-123',winsound.SND_FILENAME)
sound_dict = {"winsound.PlaySound('9_mm_gunshot-mike-koenig-123',winsound.SND_FILENAME)" : "9 mm gunshot was found!",
              "winsound.PlaySound('40_smith_wesson_single-mike-koenig',winsound.SND_FILENAME)" :"40 smith wesson was found!",
              "winsound.PlaySound('380_gunshot_single-mike-koenig',winsound.SND_FILENAME)": "12 Ga Winchester shotgun was found!",
              "winsound.PlaySound('380_gunshot',winsound.SND_FILENAME)": "380 gunshot was found!",
              "winsound.PlaySound('flute',winsound.SND_FILENAME)": "Flute sound was found!",
              "winsound.PlaySound('drums',winsound.SND_FILENAME)" : "Drums sound was found!"
              }
with open('Response.txt', 'a') as the_file:
    for key,value in sound_dict.items():
        key
        ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title",1 )




#Version1
"""
import ctypes  # An included library with Python install.
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title",1 )
"""


# version2
"""
from tkinter import * #If you get an error here, try Tkinter not tkinter

def Dialog1Display():
    Dialog1 = Toplevel(height=1000, width=1000) #Here

def Dialog2Display():
    Dialog2 = Toplevel(height=2000, width=2000) #Here

master=Tk()

Button1 = Button(master, text="Small", command=Dialog1Display)
Button2 = Button(master, text="Big", command=Dialog2Display)

Button1.pack()
Button2.pack()
master.mainloop()

"""

#version3
"""
from tkinter import *

WELCOME_MSG = '''Welcome to this event.

Your attendance has been registered.

Don't forget your free lunch.'''
WELCOME_DURATION = 3

def welcome():
    top = Toplevel()
    top.title('Welcome')
    Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
    top.after(WELCOME_DURATION, top.destroy)

root = Tk()
Button(root, text="Click to register", command=welcome).pack()

root.mainloop()

"""