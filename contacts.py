from tkinter import *
from tkinter import messagebox
import sqlite3
from addcontacts import AddContacts

con = sqlite3.connect('database.db')
cur = con.cursor()

class Contacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry('700x700+500+200')
        self.title('Contacts')
        self.resizable(False, False)

        self.top = Frame(self, height = 150, bg='#a38f6a')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=550, bg="#5b4824")
        self.bottom.pack(fill=X)

        #top
        self.top_image = PhotoImage(file="images/contact.png")
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=70, y=40)

        self.heading = Label(self.top, text="Contacts", font="Neon 15 bold", bg="#a38f6a", fg="#efe9de")
        self.heading.place(x=170, y=60)

        self.contList = Listbox(self.bottom, width=40, height=27)
        self.contList.grid(row=0, column=0, padx=(40, 0))
        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)
        self.scroll.config(command=self.contList.yview)
        self.contList.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=1, sticky=N+S)

        contactRecords = cur.execute("select * from 'contactList' order by firstName Asc").fetchall()
        sn = 0
        for contactRecord in contactRecords:
            self.contList.insert(sn, str(contactRecord[1]) + " " + str(contactRecord[2]) + " " + str(contactRecord[3]))
            sn += 1
        #buttons
        btnAdd = Button(self.bottom, text='Add Contact', width=15, font='Sans 12 bold', command=self.addCons)
        btnAdd.grid(row=0, column=2, padx=40, pady=10, sticky=N)

        # btnUpdate = Button(self.bottom, text='Update', width=15, font='Sans 12 bold')
        # btnUpdate.grid(row=0, column=2, padx=40, pady=60, sticky=N)

        # btnDisplay = Button(self.bottom, text='List Contacts', width=15, font='Sans 12 bold')
        # btnDisplay.grid(row=0, column=2, padx=40, pady=60, sticky=N)

        btnDelete = Button(self.bottom, text='Delete', width=15, font='Sans 12 bold', command=self.deleteContact)
        btnDelete.grid(row=0, column=2, padx=40, pady=60, sticky=N)
    
    def deleteContact(self):
        selectedContact = self.contList.curselection()
        contact = self.contList.get(selectedContact)
        
        deleteQueryName = contact.split(" ")[0]
        deleteQueryNumber = contact.split(" ")[2]

        deleteQuery = "SELECT id FROM contactList WHERE firstName LIKE ? AND phoneNumber LIKE ?;"
        deleteQueryID = cur.execute(deleteQuery, (deleteQueryName, deleteQueryNumber)).fetchall()

        query = "DELETE FROM contactList WHERE id = {}".format(deleteQueryID[0][0])
        warnn = messagebox.askquestion("Warning", "Are you sure about deleting this contact?")
        if warnn == 'yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("Success", "Contact Deleted")
                self.destroy()
            except Exception as e:
                messagebox.showinfo("Info", str(e))
    def addCons(self):
        addCon = AddContacts()
        self.destroy()
