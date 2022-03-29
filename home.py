from tkinter import *
from sorting_menu import *

WIN = Tk()
WIN.title("Algorithm Visualiser")
WIN.geometry("900x600")

def onSorting():
    onSortingCall(WIN)

sorting_btn = Button(WIN, text="Sorting", command=onSorting)
sorting_btn.grid(row=10, column=10)

WIN.mainloop()