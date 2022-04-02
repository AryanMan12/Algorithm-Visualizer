from tkinter import *
import sorting

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

        b1 = Button(self.sorting_container, text="Quick Sort", command= self.onQuick)
        b1.pack()

        b2 = Button(self.sorting_container, text="Merge Sort", command= self.onMerge)
        b2.pack()

        b3 = Button(self.sorting_container, text="Selection Sort", command= self.onSelection)
        b3.pack()

        b4 = Button(self.sorting_container, text="Bubble Sort", command= self.onBubble)
        b4.pack()

        b5 = Button(self.sorting_container, text="Insertion Sort", command= self.onInsertion)
        b5.pack()
    
    def onBack(self):
        self.sorting_container.destroy()
        home()

    def onQuick(self):
        s = sorting.sorter("Quick")
        s.main()
    def onMerge(self):
        s = sorting.sorter("Merge")
        s.main()
    def onSelection(self):
        s = sorting.sorter("Selection")
        s.main()
    def onBubble(self):
        s = sorting.sorter("Bubble")
        s.main()
    def onInsertion(self):
        s = sorting.sorter("Insertion")
        s.main()

home()
WIN.mainloop()

