#small GUI Window
# from tkinter import *

# root = Tk()
# root.mainloop()


#GUI Example
# from tkinter import *

# # creating root window 
# root = Tk()

# # customizing root window title 
# root.title("Welcome to Python Lobby")
# # customizing root window dimension 
# root.geometry('1300x200')

# root.mainloop()


# from tkinter import *

# # creating root window
# root = Tk()

# # customizing root window title
# root.title("Welcome to Python Lobby")
# # customizing root window dimension
# root.geometry('250x200')
# name = "We are Python Lobby-ian"

# # placing label to our GUI app
# lbl = Label(root, text = name, font=("Helvetica", 30), fg = 'white' , bg='black')

# lbl.place(x=100,y=100)

# root.mainloop()




# from tkinter import *

# # creating root window
# root = Tk()
# root.title("Welcome to Python Lobby")
# # function defined which is called when button is clicked
# def clicked():
#     print("I am clicked")
# # placing Button to our GUI app
# btn = Button(root, text="Click me", command = clicked)
# btn.pack()
# root.geometry('250x200')
# root.mainloop()


# Importing Tkinter module
# from tkinter import *

# root = Tk()
# root.title("PythonLobby")

# # Tkinter string variable it can store any string value
# value1 = StringVar(root, "1")

# rbtn1 = Radiobutton(root, text="Radio Button 1", variable = value1 , value="1")
# rbtn1.pack()
# rbtn2 = Radiobutton(root, text="Radio Button 2", variable = value1 , value="2")
# rbtn2.pack()
# rbtn3 = Radiobutton(root, text="Radio Button 3", variable = value1 , value="3")
# rbtn3.pack()

# root.geometry("250x200")
# mainloop()


# from tkinter import *

# root = Tk()
# root.title("PythonLobby")
# w = Label(root, text='PythonLobby.Com', font="60")
# w.pack()

# Checkbox1 = IntVar()
# Checkbox2 = IntVar()

# Button0 = Checkbutton(root, text="Learning",
#                       variable=Checkbox1,
#                       onvalue=1,
#                       offvalue=0,
#                       height=3,
#                       width=12)

# Button1 = Checkbutton(root, text="Tutorial",
#                       variable=Checkbox2,
#                       onvalue=1,
#                       offvalue=0,
#                       height=3,
#                       width=12)

# Button0.pack()
# Button1.pack()

# root.geometry("320x220")
# mainloop() 

# from tkinter import *
# from tkinter import ttk

# root = Tk()
# label = Label(root, text="This is Image").pack(side=TOP, pady=10)

# path = PhotoImage(file="C:/Users/ACER/OneDrive/Desktop/python/vscode.png")
# label_image = Label(root, image=path,width=400, height=400)
# label_image.pack()

# root.geometry("600x440")
# root.title("PythonLobby.com")
# root.mainloop()


# from tkinter import * 
# from tkinter.ttk import * 
# from time import strftime

# # creating tkinter window
# root = Tk()
# root.title('Menu Demonstration')

# # Creating Menubar
# menubar = Menu(root)

# # Adding File Menu and commands
# file = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label ='File', menu = file)
# file.add_command(label ='New File', command = None)
# file.add_command(label ='Open...', command = None)
# file.add_command(label ='Save', command = None)
# file.add_separator()
# file.add_command(label ='Exit', command = root.destroy)

# # Adding Edit Menu and commands
# edit = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label ='Edit', menu = edit)
# edit.add_command(label ='Cut', command = None)
# edit.add_command(label ='Copy', command = None)
# edit.add_command(label ='Paste', command = None)
# edit.add_command(label ='Select All', command = None)
# edit.add_separator()
# edit.add_command(label ='Find...', command = None)
# edit.add_command(label ='Find again', command = None)

# # Adding Help Menu
# help_ = Menu(menubar, tearoff = 0)
# menubar.add_cascade(label ='Help', menu = help_)
# help_.add_command(label ='Tk Help', command = None)
# help_.add_command(label ='Demo', command = None)
# help_.add_separator()
# help_.add_command(label ='About Tk', command = None)

# # display Menu
# root.config(menu = menubar)
# mainloop()


# from tkinter import *
# #setting up parent window
# root = Tk()

# canvas = Canvas(root, bg="yellow", width=150, height=250)
# canvas.pack()
# rectangle= canvas.create_rectangle(30,20,140,90, fill="light green")
# root.geometry("350x220")
# root.title("PythonLobby.com")
# root.mainloop()


# from tkinter import *
# #setting up parent window
# root = Tk()

# canvas = Canvas(root, bg="yellow", width=150, height=250)
# canvas.pack()
# line = canvas.create_line(30,50,100,5,23,30, width=5, fill="red")

# root.geometry("350x220")
# root.title("PythonLobby.com")
# root.mainloop()


# from tkinter import *
# #setting up parent window
# root = Tk()

# canvas = Canvas(root, bg="yellow", width=150, height=250)
# canvas.pack()
# line = canvas.create_line(70,150,140,5)

# root.geometry("350x220")
# root.title("PythonLobby.com")
# root.mainloop()

# from tkinter import *
# from tkinter import ttk

# root = Tk()

# # ListBox Widget
# listbox = Listbox(root, width=45, height=15)
# listbox.pack(pady=20)

# #adding widget to Tab
# listbox.insert(0, "C")
# listbox.insert(1, "C++")
# listbox.insert(2, "Java")
# listbox.insert(3, "Python")

# root.geometry("400x240")
# root.title("PythonLobby.com")
# root.mainloop()

# from tkinter import *
# from tkinter import ttk

# root = Tk()

# # ListBox Widget
# listbox = Listbox(root, width=45, height=15, selectmode=MULTIPLE)
# listbox.pack(pady=20)

# #adding widget to Tab
# listbox.insert(0, "C")
# listbox.insert(1, "C++")
# listbox.insert(2, "Java")
# listbox.insert(3, "Python")

# root.geometry("400x240")
# root.title("PythonLobby.com")
# root.mainloop()

# from tkinter import *
# root = Tk()

# def callback():
#     text = textEditor.get(0.1,END)
#     print(text)

# textEditor = Text(root, width=43, height=10)
# textEditor.pack()

# button1 = Button(root, text="Display Text", command = callback )
# button1.pack(pady=12)

# root.geometry('350x218')
# root.title("PythonLobby")
# root.mainloop()

# from tkinter import *
# root = Tk()

# def callback():
#     text = textEditor.get(0.1,END)
#     print(text)

# textEditor = Text(root, width=43, height=10, font=(("Times"), 10,"bold"), wrap=WORD, fg="white", bg="black")
# textEditor.pack()

# button1 = Button(root, text="Display Text", command = callback )
# button1.pack(pady=12)

# root.geometry('350x218')
# root.title("PythonLobby")
# root.mainloop()


# from tkinter import *

# root = Tk()
# root.title("Facebook Login")
# root.geometry("400x500")
# root.configure(bg="#f0f2f5")


# title = Label(
#     root,
#     text="facebook",
#     font=("Arial", 28, "bold"),
#     fg="#1877f2",
#     bg="#f0f2f5"
# )
# title.pack(pady=30)

# email = Entry(root, font=("Arial", 12), width=30)
# email.insert(0, "Email address or phone number")
# email.pack(pady=10, ipady=8)

# password = Entry(root, font=("Arial", 12), width=30, show="*")
# password.pack(pady=10, ipady=8)

# login_btn = Button(
#     root,
#     text="Log In",
#     bg="#1877f2",
#     fg="white",
#     font=("Arial", 12, "bold"),
#     width=25
# )
# login_btn.pack(pady=15)

# forgot = Label(
#     root,
#     text="Forgotten password?",
#     fg="#1877f2",
#     bg="#f0f2f5",
#     cursor="hand2"
# )
# forgot.pack(pady=10)

# create_btn = Button(
#     root,
#     text="Create New Account",
#     bg="#42b72a",
#     fg="white",
#     font=("Arial", 11, "bold"),
#     width=20
# )
# create_btn.pack(pady=20)

# root.mainloop()


from tkinter import *

root = Tk()
root.title("Facebook Login")
root.geometry("500x400")
root.configure(bg="#f0f2f5")

title = Label(
    root,
    text="facebook",
    font=("Helvetica", 30, "bold"),
    fg="#1877F2",
    bg="#f0f2f5"
)
title.place(x=170, y=30)

desc = Label(
    root,
    text="Log in to Facebook",
    font=("Arial", 12),
    bg="#f0f2f5"
)
desc.place(x=180, y=80)

email_lbl = Label(root, text="Email or Phone", bg="#f0f2f5")
email_lbl.place(x=100, y=130)

email_entry = Entry(root, width=35)
email_entry.place(x=100, y=155)

password_lbl = Label(root, text="Password", bg="#f0f2f5")
password_lbl.place(x=100, y=190)

password_entry = Entry(root, width=35, show="*")
password_entry.place(x=100, y=215)

def login():
    email = email_entry.get()
    password = password_entry.get()

    print("Email:", email)
    print("Password:", password)

login_btn = Button(
    root,
    text="Log In",
    command=login,
    bg="#1877F2",
    fg="white",
    width=20
)
login_btn.place(x=160, y=260)

forgot = Label(
    root,
    text="Forgotten Password?",
    fg="blue",
    bg="#f0f2f5"
)
forgot.place(x=180, y=310)

root.mainloop()