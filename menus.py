from tkinter import *

WIN = Tk()
WIN.title("Algorithm Visualiser")
WIN.geometry("900x600")


class home():
    def __init__(self):
        self.home_container = Frame(WIN)
        self.home_container.pack(side = "top", fill = "both", expand = True)

        self.sorting_btn = Button(self.home_container, text="Sorting", command=self.onSorting)
        self.sorting_btn.pack()

    def onSorting(self):
        self.home_container.destroy()
        sorting_menu()


class sorting_menu():
    def __init__(self):
        self.sorting_container = Frame(WIN)
        self.sorting_container.pack(side = "top", fill = "both", expand = True)

        l = Label(self.sorting_container, text="Abcd")
        l.pack()

        b = Button(self.sorting_container, text="Back", command= self.onBack)
        b.pack()
    
    def onBack(self):
        self.sorting_container.destroy()
        home()

home()
WIN.mainloop()

