from tkinter import *
from tkinter import font
from tkinter import messagebox
import sorting

WIN = Tk()
WIN.title("Algorithm Visualiser")
WIN.geometry("900x600")
WIN.resizable(0,0)


class home():
    def __init__(self):
        self.home_container = Frame(WIN)
        self.home_container.pack(side = "top", fill = "both", expand = True)

        self.app_name=Label(self.home_container,text='Algorithm visualizer',font=("Arial",30))
        self.app_name.place(x=280,y=70)

        self.sorting_btn = Button(self.home_container, text="Sorting", command=self.onSorting, width=20)
        self.sorting_btn['font']=font.Font(size=20)
        self.sorting_btn.place(x=290,y=200)

        self.tree_btn = Button(self.home_container, text="Tree", command=self.onSorting, width=20)
        self.tree_btn['font']=font.Font(size=20)
        self.tree_btn.place(x=290,y=300)

        self.graph_btn = Button(self.home_container, text="Graph", command=self.onSorting, width=20)
        self.graph_btn['font']=font.Font(size=20)
        self.graph_btn.place(x=290,y=400)

    def onSorting(self):
        self.home_container.destroy()
        sorting_menu()


class sorting_menu():
    def __init__(self):
        self.sorting_container = Frame(WIN)
        self.sorting_container.pack(side = "top", fill = "both", expand = True)
        
        self.enteredList = False
        self.LIST = []
        self.RANGE = 0
        
        sorting_label = Label(self.sorting_container, text="Sorting", font=("Ariel", 30))
        sorting_label.pack()

        enter_range_btn = Button(self.sorting_container, text="Generate List", command=self.onEnterRange)
        enter_range_btn.pack()

        enter_list_btn = Button(self.sorting_container, text="Enter List", command=self.onEnterList)
        enter_list_btn.pack()

        self.enter_list_label = Label(self.sorting_container, text="Enter List of Numbers (seperated by space)")
        self.enter_list_entry = Entry(self.sorting_container)

        self.enter_range_label = Label(self.sorting_container, text="Enter Range")
        self.enter_range_entry = Entry(self.sorting_container)

        back_btn = Button(self.sorting_container, text="Back", command= self.onBack)
        back_btn.pack()

        quick_sort_btn = Button(self.sorting_container, text="Quick Sort", command= self.onQuick)
        quick_sort_btn.pack()

        merge_sort_btn = Button(self.sorting_container, text="Merge Sort", command= self.onMerge)
        merge_sort_btn.pack()

        selection_sort_btn = Button(self.sorting_container, text="Selection Sort", command= self.onSelection)
        selection_sort_btn.pack()

        bubble_sort_btn = Button(self.sorting_container, text="Bubble Sort", command= self.onBubble)
        bubble_sort_btn.pack()

        insertion_sort_btn = Button(self.sorting_container, text="Insertion Sort", command= self.onInsertion)
        insertion_sort_btn.pack()
    
    def onEnterRange(self):
        self.enter_list_label.pack_forget()
        self.enter_list_entry.pack_forget()
        self.enter_range_label.pack()
        self.enter_range_entry.pack()
        self.enteredList = False

    def onEnterList(self):
        self.enter_range_label.pack_forget()
        self.enter_range_entry.pack_forget()
        self.enter_list_label.pack()
        self.enter_list_entry.pack()
        self.enteredList = True

    def onBack(self):
        self.sorting_container.destroy()
        home()

    def getValues(self):
        if self.enteredList:
            try:
                self.LIST = list(map(int, self.enter_list_entry.get().strip().split(" ")))
                return self.LIST
            except:
                messagebox.showerror("Error","Enter a valid list")
        else:
            try:
                if int(self.enter_range_entry.get()) <= 1 or int(self.enter_range_entry.get()) > 800:
                    messagebox.showerror("Error","Range should be greater than 1 or less than 800")
                else:
                    self.RANGE = int(self.enter_range_entry.get())
                    return self.RANGE
            except:
                messagebox.showerror("Error","Enter a valid Number")

    def onQuick(self):
        val = self.getValues()
        if val ==None:
            pass
        else:
            s = sorting.sorter("Quick", val)
            s.main()

    def onMerge(self):
        val = self.getValues()
        if val ==None:
            pass
        else:
            s = sorting.sorter("Merge", val)
            s.main()

    def onSelection(self):
        val = self.getValues()
        if val ==None:
            pass
        else:
            s = sorting.sorter("Selection", val)
            s.main()

    def onBubble(self):
        val = self.getValues()
        if val ==None:
            pass
        else:
            s = sorting.sorter("Bubble", val)
            s.main()

    def onInsertion(self):
        val = self.getValues()
        if val ==None:
            pass
        else:
            s = sorting.sorter("Insertion", val)
            s.main()

home()
WIN.mainloop()

