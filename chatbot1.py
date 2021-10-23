from tkinter import *
from scrollableframe import ScrollableFrame
import datetime as dt
import random
import sql_signup_login as s

global root, frame, user_input, textbox, enter, itpt, temp, str_mail
global paswrd, bdays, meet_t
global prevjoke
prevjoke = ""

def init():
    global paswrd, bdays, meet_t
    global str_mail
    s.createDatabase()
    s.createTable()
    paswrd, bdays, meet_t = s.bringData(str_mail)
    
def init_gui(user_mail):
    global str_mail
    str_mail = user_mail
    init()
    global root, frame, user_input, textbox, enter, itpt
    root = Tk()
    root.title(f"Buddy : Hi {user_mail}")
    root.geometry("500x600")
    root.focus()
    root.rowconfigure(0, weight=4)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)

    itpt = StringVar()
    frame = ScrollableFrame(root)
    Label(frame.scrollable_frame, text="Hi there !", font=("Poppins", 14)).pack()
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    user_input = Frame(root, bg="grey")
    user_input.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    user_input.rowconfigure(0, weight=1)
    user_input.columnconfigure(0, weight=5)
    user_input.columnconfigure(1, weight=1)

    textbox = Entry(user_input, text="Hi", font=("Poppins", 14), highlightthickness=1, highlightcolor="grey")
    textbox.grid(row=0, column=0, sticky="nsew")

    enter = Button(user_input, text="Send", font=("Poppins", 14), fg="white", bg="#5945b2", command=send)
    enter.grid(row=0, column=1, sticky="nsew")

    heyBuddy()


def send():
    global itpt, c, prev
    itpt.set(textbox.get())
    c = 1


def click(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, 'end')


def leave(entry, placeholder):
    if entry.get() == "":
        entry.delete(0, 'end')
        entry.insert(0, placeholder, )
    else:
        enter.config(state=NORMAL)
    root.focus()


def uinput(msg):
    global itpt, c
    textbox.bind("<FocusIn>", lambda event, entry=textbox, plc=msg: click(entry, plc))
    textbox.bind("<FocusOut>", lambda event, entry=textbox, plc=msg: leave(entry, plc))
    textbox.delete(0, 'end')
    textbox.insert(0, msg, )
    root.focus()
    enter.wait_variable(itpt)
    display(f"{msg} {itpt.get()}")
    return itpt.get()


def display(msg):
    label = Label(frame.scrollable_frame, text=msg, font=("Poppins", 14), border=1, justify=LEFT)
    if msg[0:3] == "Bot":
        label.pack()
    else:
        label.pack()


def newline():
    global textbox, enter
    # textbox.delete(0, 'end')
    # textbox.insert(0, "Enter the command : ", )
    s = uinput("Enter something : ")
    return s


def notesW():
    namee = uinput("Enter the file name : ")
    FileName = namee + ".txt"
    file = open(FileName, "a+")
    try:
        file1 = open(FileName, "r")
        etext = file1.read()
        display(etext)
    except:
        display("CREATING NEW FILE ...")
    text = uinput("Enter your notes : ")
    text = text + "\n"
    file.write(text)
    file.close()


def notesR():
    try:
        namee = uinput("Enter the file to read : ")
        FileName = namee + ".txt"
        file = open(FileName, "r")
        text = file.read()
        display(text)
        file.close()
    except:
        display("No such file with this name exists !!")


def heyBuddy():
    global paswrd, bdays, meet_t, prevjoke, str_mail
    name = ""
    f = 1
    paswrd = {}
    bdays = {}
    meet_t = {}
    display("Bot : _______Welcome to Chat Bot_______")
    display("Enter \h for help")
    while f == 1:
        s1 = newline().lower()
        c = []
        if s1[0] == "\\":
            if s1[1] == "n":
                while True:
                    display("Bot : ________For Notes________"
                            "\nBot : 1. If u want to write/add notes "
                            "\nBot : 2. If u want to read/view notes "
                            "\nBot : 3. You want to exit ")
                    op = int(uinput("Enter your choice :"))
                    if op == 1:
                        notesW()
                    elif op == 2:
                        notesR()
                    elif op == 3:
                        break
                    else:
                        print("Bot : Your have enterted invalid option.")

            elif s1[1] == "p":
                while True:
                    display("Bot : ______Search and saving passwords______"
                            "\nBot : 1.Search for a specific password"
                            "\nBot : 2.Show all of the password"
                            "\nBot : 3.Add a new password"
                            "\nBot : 4.Exit")
                    op = int(uinput("Enter your choice :"))
                    if op == 1:
                        if len(paswrd.keys()) == 0:
                            display("Bot : We have no data of password to show.")
                        else:
                            web = uinput("Enter the website name :")
                            password = paswrd.get(web, "Bot : We dont have data for this website.")
                            display(f"Bot : The password is : {password}")
                    elif op == 2:
                        if len(paswrd.keys()) == 0:
                            display("Bot : We have no data of password to show.")
                        else:
                            display(f"Bot : All of the password's are :")
                            display("{:<10} {:<10}".format('WEBSITE', 'PASSWORD'))
                            for webnm, passwrd in paswrd.items():
                                display("{:<10} {:<10}".format(webnm, passwrd))
                    elif op == 3:
                        web = uinput("Enter the website name (whose password u want to save) :")
                        password = uinput("Enter the password for it :")
                        paswrd[web] = password
                        display("Bot : Data added successfully!!")
                    elif op == 4:
                        display("Bot : Thanks for saving the password's.")
                        break
                    else:
                        display("Bot : Your have enterted invalid option.")
            elif s1[1] == "t":
                # {date(obj) : {datetime(obj):event}}
                while True:
                    display("Bot : ______Meeting Time Management______"
                            "\nBot : 1.Search for a Meeting "
                            "\nBot : 2.Show all the Meetings"
                            "\nBot : 3.Add a new Meeting"
                            "\nBot : 4.Exit")
                    op = int(uinput("Enter your choice :"))
                    if op == 1:
                        if len(meet_t.keys()) == 0:
                            display("Bot : U dont have any meetings on any of the days .\nEnjoy :)")
                        else:
                            while True:
                                display("Bot : 1. Do u want to search by date "
                                        "\nBot : 2. Do u want to search by time "
                                        "\nBot : 3. Do u want to search by event "
                                        "\nBot : 4. Exit ")
                                ch = int(uinput("Enter your choice :"))
                                if ch == 1:
                                    while True:
                                        try:
                                            date_m = dt.datetime.strptime(uinput("Enter the date (dd/mm/yy) :"), "%d/%m/%y")
                                            if date_m not in meet_t:
                                                display(f"Bot : No meetings on {date_m}.\nEnjoy :)")
                                            else:
                                                display("Bot : ")
                                                display("{:<10} {:<10}".format('TIME', 'EVENT'))

                                                for time, event in meet_t[date_m].items():
                                                    display("{:<10} {:<10}".format(time, event))
                                            break
                                        except:
                                            display("Incorrect date format")
                                elif ch == 2:
                                    time_m = uinput("Enter the time (e.g: write 1:20pm as 1320) :")
                                    display("Bot : ")
                                    display("{:<10} {:<10}".format('DATE', 'EVENT'))
                                    for date, sched in meet_t.items():
                                        if time_m in sched:
                                            display("{:<10} {:<10}".format(dt.datetime.strftime(date, "%d/%m/%y"),
                                                                           sched[time_m]))
                                elif ch == 3:
                                    event_m = uinput("Enter what the event name is :")
                                    display("Bot : ")
                                    display("{:<10} {:<10} {:<10}".format('DATE', 'TIME', 'EVENT'))
                                    for date, sched in meet_t.items():
                                        for time, event in sched.items():
                                            if event.find(event_m) != -1:
                                                display("{:<10} {:<10} {:<10}".format(
                                                    dt.datetime.strftime(date, "%d/%m/%y"), time, event))
                                elif ch == 4:
                                    display("Bot : Thanks for using this search feature.")
                                    break
                                else:
                                    display("Bot : Your have enterted invalid option.")
                    elif op == 2:
                        if len(meet_t.keys()) == 0:
                            display("Bot : U dont have any meetings on any of the days .\nEnjoy :)")
                        else:
                            display("Bot : Here are all your meetings : ")
                            display("{:<10} {:<10} {:<10}".format('DATE', 'TIME', 'EVENT'))
                            for date, sched in meet_t.items():
                                for time, event in sched.items():
                                    display("{:<10} {:<10} {:<10}".format(dt.datetime.strftime(date, "%d/%m/%y"), time, event))
                                display("-" * 45)
                    elif op == 3:
                        while True:
                            try:
                                date_m = dt.datetime.strptime(uinput("Enter the date (dd/mm/yy) :"), "%d/%m/%y")
                                time_m = uinput("Enter the time (e.g: write 1:20pm as 1320) :")
                                event = uinput("Enter the description of the meeting :")
                                if date_m in meet_t:
                                    sched = meet_t[date_m]
                                    if time_m not in sched:
                                        sched[time_m] = event
                                    else:
                                        display(f"Bot : A meeting is already scheduled at this time")
                                        y_or_n = uinput("Do you want to override with your new meeting ? [Y/N] : ").lower()
                                        if y_or_n == "y":
                                            sched[time_m] = event
                                else:
                                    meet_t[date_m] = {time_m: event}
                                display("Bot : Meeting schedule added successfully!!")
                                break
                            except:
                                display("Incorrect date format")
                    elif op == 4:
                        display("Bot : Thanks for using this meeting time manager.")
                        break
                    else:
                        display("Bot : Your have enterted invalid option.")
            elif s1[1] == "b":
                while True:
                    display("Bot : ______Search and saving birthdays______"
                            "\nBot : 1.Search for a person's birthday"
                            "\nBot : 2.Show all the birthdays"
                            "\nBot : 3.Add a new birthday"
                            "\nBot : 4.Exit")
                    op = int(uinput("Enter your choice :"))
                    if op == 1:
                        if len(bdays.keys()) == 0:
                            display("Bot : You haven't added any birthdays yet !")
                        else:
                            while True:
                                display("Bot : 1. Do u want to search by date "
                                        "\nBot : 2. Do u want to search by name "
                                        "\nBot : 3. Exit ")
                                ch = int(uinput("Enter your choice :"))
                                if ch == 1:
                                    birth_date = uinput("Enter the birthdate (dd/mm) :")
                                    if birth_date not in bdays:
                                        display(f"Bot : No one has their birthday on {birth_date}.")
                                    else:
                                        display(f"Bot : People who have their birthday on {birth_date} are :")
                                        display(f"{'NAME':<10}")
                                        for name in bdays[birth_date]:
                                            display(f"{name:<10}")
                                elif ch == 2:
                                    name_find = uinput("Enter the name whose birthdate u want to find :").lower().strip()
                                    for date, names in bdays.items():
                                        for name in names:
                                            if name == name_find:
                                                display(f"Bot : {name} has their birthday on {date}")
                                elif ch == 3:
                                    display("Bot : Thanks for using searching feature.")
                                    break
                                else:
                                    display("Bot : Your have entered invalid option.")
                    elif op == 2:
                        if len(bdays.keys()) == 0:
                            display("Bot : We have nothing to show to u as no birthday is there.")
                        else:
                            display("Bot : Here are all your birthdays : ")
                            display("{:<10} {:<10}".format('BIRTHDATE', 'NAME'))
                            for date, names in bdays.items():
                                for name in names:
                                    display("{:<10} {:<10}".format(date, name))
                                display("-" * 10)
                    elif op == 3:
                        # {birthdate : []}
                        person_name = uinput("Enter the name which has to be added :")
                        birth_date = uinput("Enter the birthdate (dd/mm) :")
                        if birth_date in bdays:
                            bdays[birth_date].append(person_name)
                        else:
                            bdays[birth_date] = [person_name]
                        display("Bot : Birthday added successfully!!")
                    elif op == 4:
                        display("Bot : Thanks for saving the birthdays.")
                        break
                    else:
                        display("Bot : Your have enterted invalid option.")
            elif s1[1] == "j":
                with open("jokes.txt", "r") as file:
                    lines = file.readlines()
                    joke = random.choice(lines)
                    while joke == prevjoke:
                        joke = random.choice(lines)
                    prevjoke = joke
                    display(f"Bot : {joke}")
            elif s1[1] == "h":
                display("Bot : The Commands that we have is :"
                        "\n \\n for Notes ,\n \\p for Password handling ,\n \\b for Birthday's ,\n \\t for Meeting Time Management ,\n \\h for Help ,\n \\e for Exit ,\n \\j for Jokes")
            elif s1[1] == "e":
                display("Bot : Bye bye see u later, Thank you for using our services. Hope u enjoyed it.")
                s.sendData((paswrd,bdays,meet_t),str_mail)
                exit()
            else:
                 display("Bot : Invalid Command !!"
                        "\nThe Commands that we have is :"
                        "\n \\n for Notes ,\n \\p for Password handling ,\n \\b for Birthday's ,\n \\t for Meeting Time Management ,\n \\h for Help ,\n \\e for Exit ,\n \\j for Jokes")

        elif s1 == "bye" or s1 == "exit" or s1 == "see u later" or s1 == "see you later" or s1 == "talk to u later" or s1 == "talk to you later":
            display("Bot : Bye bye see u later, Thank you for using our services. Hope u enjoyed it.")
            s.sendData((paswrd,bdays,meet_t),str_mail)
            exit()
        elif s1 == "hi" or s1 == "hey" or s1 == "hello" or s1 == "ssup":
            display("Bot : Hey, Nice meeting u. How can i help u?")

        elif s1 == "what are the commands" or s1 == "commands" or s1 == "help":
            display("Bot : The Commands that we have is :"
                    "\n\\n for Notes ,\n \\p for Password handling ,\n \\b for Birthday's ,\n \\t for Meeting Time Management ,\n \\h for Help ,\n \\e for Exit ,\n \\j for Jokes")

        elif s1 == "what is the date today" or s1 == "what is today" or s1 == "today" or s1 == "what is the date today?" or s1 == "what is today?" or s1 == "today?" or s1 == "what is today's date?" or s1 == "today's date":
            today = dt.date.today()
            display(f"Bot : Today date is: {today}")

        elif s1[0:11] == "my name is ":
            user_name = s1[11:]
            display(f"Bot : Hey {user_name}, Nice meeting u. How can i help u?")

        else:
            display("Bot : Invalid Command !!"
                    "\nThe Commands that we have is :"
                    "\n \\n for Notes ,\n \\p for Password handling ,\n \\b for Birthday's ,\n \\t for Meeting Time Management ,\n \\h for Help ,\n \\e for Exit ,\n \\j for Jokes")

    root.mainloop()
