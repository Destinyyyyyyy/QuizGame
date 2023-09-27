from tkinter import *
import tkinter.messagebox as messagebox

gui = Tk()


gui.title("Quiz Game")
gui.geometry('1920x1080')
gui.configure(bg= '#99d2ff')

username_entry = None
password_entry = None

def login():
    username = username_entry.get()
    password = username_entry.get()

    
    with open("database.txt", "r") as file: 
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password = stored_password:
                messagebox.showinfo("Login Successful", "Welcome, " + username)
                #Code to transition to Quizgame
                break
        else: 
            messagebox.showerror("Login Failed", "Invalid Username or Password")

def register(): 
    username = username_entry.get()
    password = password_entry.get()

    with open("database.txt", "r") as file: 
        for line in file:
            stored_username, _ = line.strip().split(',')





gui.mainloop()



