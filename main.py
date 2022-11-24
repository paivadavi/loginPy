from tkinter import *
import sqlite3 as sql

# Database functions
def login():
    pass


root = Tk()
root.geometry("450x300")
root.configure(bg="darkblue")

username = Label(root, text="Username")
username.configure(fg="white", bg="darkblue", font="roboto")
username.place(x=30, y=50)

username_entry = Entry(root, width=30)
username_entry.place(x=30, y=75)

password = Label(root, text="Password")
password.configure(fg="white", bg="darkblue", font="roboto")
password.place(x=30, y=125)

password_entry = Entry(root, width=30)
password_entry.place(x=30, y=150)

button = Button(root, text="Log in")
button.configure(fg="white", width=27, bg="darkblue", function=)
button.place(x=30, y=200)

root.mainloop()
