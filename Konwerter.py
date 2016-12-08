from Tkinter import *
from tkMessageBox import *

class EntryDemo( Frame ):

    def __init__(self):

        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Testowanie pol tekstowych")
        self.master.geometry("325x100")

        self.frame1=Frame(self)
        self.frame1.pack(pady=5)
        self.var = IntVar()
        for text, value in [("BIN", 0), (u'HEX', 1), (u'OCT', 2)]:
            Radiobutton(self, text=text, value=value, variable=self.var).pack(anchor=W)

        self.var.set(3)
        print self.var.get()

        self.text1 = Entry (self.frame1, name="tekst 1")
        self.text1.bind("<Return>", self.showContents)
        self.text1.pack(side=LEFT, padx=5)

        self.button = Button(self.frame1,command=self.showContents)
        self.button.pack(side =LEFT,padx=5)




    def showContents(self, event):
        theName=event.widget.winfo_name()
        theContents = event.widget.get()
        if(self.var.get()==0):
            ret = bin(int(theContents))
            showinfo("komunikat", ret+" BIN")
        elif(self.var.get()==1):
            ret = hex(int(theContents))
            showinfo("komunikat", ret + " HEX")
        else:
            ret = oct(int(theContents))
            showinfo("komunikat", ret + " OCT")


def showContents(self):
    if (self.var.get() == 0):
        ret = bin(int(self.var.get()))
        showinfo("komunikat", ret + " BIN")
    elif (self.var.get() == 1):
        ret = hex(int(self.var.get()))
        showinfo("komunikat", ret + " HEX")
    else:
        ret = oct(int(self.var.get()))
        showinfo("komunikat", ret + " OCT")

def main():
    EntryDemo().mainloop()
if __name__ == "__main__":
    main()

