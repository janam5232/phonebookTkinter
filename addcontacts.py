from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect(database='database.db')
cur = con.cursor()

class AddContacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry('700x700+650+200')
        self.title('Add Contact')
        self.resizable(False, False)

        self.top = Frame(self, height = 150, bg='#a38f6a')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=550, bg="#5b4824")
        self.bottom.pack(fill=X)

        #top
        self.top_image = PhotoImage(file="images/contact.png")
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=70, y=40)

        self.heading = Label(self.top, text="Add Contact", font="Neon 15 bold", bg="#a38f6a", fg="#efe9de")
        self.heading.place(x=170, y=60)

        #name
        self.labelFirstName = Label(self.bottom, text="First Name: ", font="arial 14 bold")
        self.labelFirstName.place(x=49, y=50)

        self.enterFirstName = Entry(self.bottom, width=30, bd=4)
        self.enterFirstName.insert(0, "Enter First Name")
        self.enterFirstName.place(x=250, y=50)
        
        #lastname
        self.labelLastName = Label(self.bottom, text="Last Name: ", font="arial 14 bold")
        self.labelLastName.place(x=49, y=110)

        self.enterLastName = Entry(self.bottom, width=30, bd=4)
        self.enterLastName.insert(0, "Enter Last Name")
        self.enterLastName.place(x=250, y=110)

        #phonenumber
        self.labelPhone = Label(self.bottom, text="Email: ", font="arial 14 bold")
        self.labelPhone.place(x=49, y=170)

        self.enterPhone = Entry(self.bottom, width=12, bd=4)
        self.enterPhone.insert(0, "Enter Phone Number")
        self.enterPhone.place(x=250, y=170)

        #addButton
        button = Button(self.bottom, text="Add Contact", font="arial 14 bold", command=self.addContact)
        button.place(x=300, y=250)

    def addContact(self):
        firstName = self.enterFirstName.get()
        lastName = self.enterLastName.get()
        phone = self.enterPhone.get()

        if firstName and lastName and phone !="":
            try:
                query = "insert into 'contactList' (firstName, lastName, phoneNumber) values (?, ?, ?);"
                cur.execute(query, (firstName, lastName, phone))
                con.commit()
                messagebox.showinfo("Success", "Contact Added")
            except EXCEPTION as e:
                messagebox.showerror("Error: ", str(e))
        else:
            messagebox.showerror("Error: ", "fill all the details", icon="warning")
