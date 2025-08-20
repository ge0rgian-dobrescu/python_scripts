"""
This python script is a random password generator (using Tkinter for GUI).
"""

from tkinter import *
import random
import string
import tkinter

window = Tk()
window.title ('Password generator - V1')
window.geometry('500x250')

Label(window,font=('bold',10),text='PASSWORD GENERATOR').pack()

def password_generate(leng):
    valid_char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_' # characters of the password
    password=''.join(random.sample(valid_char,leng)) # using the random library this helps generating a random password
    l =Label(window, text = password, font=('bold', 20)) # creates a label that displays the password on the screen
    l.place(x=190,y=50)

Button(window,text='Generate',font=('normal',10), bg='yellow', command=lambda: password_generate(8)).place(x=200,y=100)

window.mainloop()

