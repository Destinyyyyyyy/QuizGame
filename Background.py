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
            if username == stored_username and password == stored_password:
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
            if username == stored_username:
                messagebox.showerror("Registeration Failed", "Username already exists")
                return
            
    
    with open("database.txt","a") as file: 
        file.write(username + "," + password + "\n")
        messagebox.showinfo("Registeration Successful", "Registeration Successful")


username_label = Label(gui, text="Username:")
username_label.pack()
username_entry = Entry(gui)
username_entry.pack()

password_label = Label(gui, text="Password:")
password_label.pack()
password_entry = Entry(gui, show="*")  
password_entry.pack()

login_button = Button(gui, text="Login", command=login)
login_button.pack()

register_button = Button(gui, text="Register", command=register)
register_button.pack()




gui.mainloop()



