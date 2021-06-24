from addcontacts import AddContacts
from tkinter import *
from contacts import Contacts

class Application(object):
    def __init__(self, master):
        self.master = master

        #frames
        self.top = Frame(master, height = 150, bg='#a38f6a')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=550, bg="#5b4824")
        self.bottom.pack(fill=X)

        #top
        self.top_image = PhotoImage(file="images/phone-list.png")
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=70, y=40)

        self.heading = Label(self.top, text="Contacts", font="Neon 15 bold", bg="#a38f6a", fg="#efe9de")
        self.heading.place(x=170, y=60)

        #buttons
        self.listButton = Button(self.bottom, width=15, text="My Contacts", font="arial 12 bold", command=self.Contacts)
        self.listButton.place(x=70, y=100)

        self.addContactButton = Button(self.bottom, width=15, text="Add Contact", font="arial 12 bold", command=self.addContactFunction)
        self.addContactButton.place(x=70, y=150)

    def Contacts(self):
        contacts = Contacts()
    
    def addContactFunction(self):
        addContactWindow = AddContacts()

def main():
    root = Tk()

    app = Application(root)
    root.title("Contacts")
    root.geometry("700x600+350+200")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()