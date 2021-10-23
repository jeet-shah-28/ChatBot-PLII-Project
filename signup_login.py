from tkinter import *
from tkinter import messagebox
import sql_signup_login as s
import re
import json
from chatbot1 import *
from PIL import Image, ImageTk

global username, email, pwd, repwd, flag, heading

method = "signup"
root = Tk()
root.title("SignUp / Login")
root.geometry("500x700")
root.attributes()

s.createDatabase()
s.createTable()


# PlaceHolder Stuff
def click(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, 'end')


def leave(entry, placeholder):
    if entry.get() == "":
        entry.delete(0, 'end')
        entry.insert(0, placeholder, )
    root.focus()


def switch(container, current):
    global login, signup, method, username, email, pwd, repwd
    # flat, groove, raised, ridge, solid, or sunken
    if current:
        heading.config(text="Signup Form")
        signup.configure(bg="#c342fa", border=0, fg="black", relief="raised")
        signup.grid(ipady=4)
        login.configure(bg="white", border=1, fg="grey", relief="sunken")
        login.grid(ipady=0)

        frame = Frame(container, bg="white")
        frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20)

        email = Entry(frame, bg="white", font=("Poppins", 14), highlightthickness=1, highlightcolor="grey")
        email.pack(fill="x", padx=20, pady=(0, 15))
        email.bind("<FocusIn>", lambda event, entry=email, plc="Email Address": click(entry, plc))
        email.bind("<FocusOut>", lambda event, entry=email, plc="Email Address": leave(entry, plc))
        email.focus()

        username = Entry(frame, bg="white", font=("Poppins", 14), highlightthickness=1, highlightcolor="grey")
        username.pack(fill="x", padx=20, pady=(0, 15))
        username.bind("<FocusIn>", lambda event, entry=username, plc="Your name": click(entry, plc))
        username.bind("<FocusOut>", lambda event, entry=username, plc="Your name": leave(entry, plc))
        username.focus()

        pwd = Entry(frame, bg="white", font=("Poppins", 14), highlightthickness=1, highlightcolor="grey")
        pwd.pack(fill="x", padx=20, pady=(0, 15))
        pwd.bind("<FocusIn>", lambda event, entry=pwd, plc="Password": click(entry, plc))
        pwd.bind("<FocusOut>", lambda event, entry=pwd, plc="Password": leave(entry, plc))
        pwd.focus()

        repwd = Entry(frame, bg="white", font=("Poppins", 14), highlightthickness=1, highlightcolor="grey")
        repwd.pack(fill="x", padx=20, pady=(0, 15))
        repwd.bind("<FocusIn>", lambda event, entry=repwd, plc="Confirm Password": click(entry, plc))
        repwd.bind("<FocusOut>", lambda event, entry=repwd, plc="Confirm Password": leave(entry, plc))
        repwd.focus()

        root.focus()

        method = "signup"
    else:
        heading.config(text="Login Form")
        login.configure(bg="#c342fa", border=0, fg="black", relief="flat")
        login.grid(ipady=4)
        signup.configure(bg="white", border=1, fg="grey", relief="sunken")
        signup.grid(ipady=0)

        frame = Frame(container, bg="white")
        frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=20)

        welcome = Label(frame, text="Welcome Back :)", bg="white", font=("Poppins SemiBold", 15))
        welcome.pack(pady=20)

        email = Entry(frame, bg="white", font=("Poppins", 14), highlightthickness=1, highlightcolor="grey")
        email.pack(fill="x", padx=20, pady=(0, 15))
        email.bind("<FocusIn>", lambda event, entry=email, plc="Email Address": click(entry, plc))
        email.bind("<FocusOut>", lambda event, entry=email, plc="Email Address": leave(entry, plc))
        email.focus()

        pwd = Entry(frame, bg="white", font=("Poppins", 14), highlightthickness=1, highlightcolor="grey")
        pwd.pack(fill="x", padx=20, pady=(0, 15))
        pwd.bind("<FocusIn>", lambda event, entry=pwd, plc="Password": click(entry, plc))
        pwd.bind("<FocusOut>", lambda event, entry=pwd, plc="Password": leave(entry, plc))
        pwd.focus()

        label = Label(frame, text="Don't have an account ? Sign Up", fg="#451090", bg="white",
                      font=("Poppins SemiBold", 14))
        label.bind("<Button-1>", lambda event: switch(container, 1))
        label.pack()

        method = "login"


# Gradient BG
img = ImageTk.PhotoImage(Image.open("gradient.jpeg").resize((500, 700)))
bg = Label(root, image=img)
bg.place(relx=0.5, rely=0.5, anchor='center')

# White Container of Form
container = Frame(root, bg="white")
container.pack(padx=30, pady=90, fill="both", expand=True)
for i in range(4):
    container.rowconfigure(i, weight=1)
container.rowconfigure(2, weight=4)
container.columnconfigure(0, weight=1)
container.columnconfigure(1, weight=1)

# Main Form
heading = Label(container, text="Signup Form", font=("Poppins SemiBold", 28), bg="white", justify=CENTER)
heading.grid(row=0, column=0, columnspan=2, sticky="ew")

login = Button(container, text="Login", font=("Poppins Regular", 18), bg="white", justify=CENTER, border=1,
               relief="solid",
               command=lambda: switch(container, 0))
login.grid(row=1, column=0, sticky="ew", padx=(20, 0))

signup = Button(container, text="Sign Up", font=("Poppins Regular", 18), bg="#c342fa", fg="white", justify=CENTER,
                border=1, relief="flat",
                command=lambda: switch(container, 1))
signup.grid(row=1, column=1, sticky="ew", padx=(0, 20))

# Sign Up frame
switch(container, 1)


def checkpwd(pwd):
    if 6 < len(pwd) < 12:
        if re.search(" ", pwd) == None:
            if re.search("[a-z]", pwd):
                if re.search("[A-Z]", pwd):
                    if re.search("\d", pwd):
                        if re.search("[^\w^\s]", pwd):
                            return True
                        else:
                            messagebox.showerror("Invaid Password !", "Atleast 1 special character needed !")
                    else:
                        messagebox.showerror("Invaid Password !", "Atleast digit needed !")
                else:
                    messagebox.showerror("Invaid Password !", "Atleast 1 uppercase needed !")
            else:
                messagebox.showerror("Invaid Password !", "Atleast 1 lowercase needed !")
        else:
            messagebox.showerror("Invaid Password !", "Spaces not allowed !!")
    else:
        messagebox.showerror("Invaid Password !", "Password length should be between 6 and 12")
    return False


def submit():
    global method, username, email, pwd, repwd, flag, submit, root

    email_str = email.get()
    p = pwd.get()
    rep = repwd.get()

    print(p, rep)

    if method == "signup":
        if re.search(r"\d", username.get()) != None:
            messagebox.showerror("Invalid input : username field",
                                 "No digits or special chars allowed !!\nEnter again !")
            username.focus()
            return
        elif not re.fullmatch(r"(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)", email.get()):
            messagebox.showerror("Invalid input : Email field", "Please enter a valid email !")
            email.focus()
            return
        elif not checkpwd(pwd.get()):
            pwd.focus()
            return

        if p != rep:
            messagebox.showerror("Invalid input : Confirm password field", "Password not matching !")
            repwd.focus()
            return

        if s.isMailPresent(email.get()):
            messagebox.showerror("Duplicate Email", "Account with this email already there !!\nPlease login !")
            return

        p1 = json.dumps({}, indent=0)
        b1 = json.dumps({}, indent=0)
        t1 = json.dumps({}, indent=0)
        s.insert(username.get(), email.get(), pwd.get(), p1, b1, t1)

        root.destroy()
        init_gui(email_str)
        heyBuddy()

    else:
        if not re.fullmatch(r"(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)", email.get()):
            messagebox.showerror("Invalid input : email", "Please enter a valid email !")
            email.focus()
            return
        if not s.isMailPresent(email.get()):
            messagebox.showerror("No account", "Account with this email does not exist !!\nPlease sign up !")
            return
        if not s.checkPass(email.get(), pwd.get()):
            messagebox.showerror("Incorrect Password", "Password not matching !!\nEnter again !")
            pwd.focus()
            return

        root.destroy()
        init_gui(email_str)
        heyBuddy()

    #     if re.search(r"\d", name):
    #         # show alertbox
    #         flag=1
    # pwd


submit = Button(container, text="Submit", font=("Poppins", 18), bg="#c342fa", fg="white", justify=CENTER, border=1,
                relief="flat",
                command=submit)
submit.grid(row=3, column=0, columnspan=2, sticky="ew", padx=30, pady=(0, 30))

root.mainloop()
