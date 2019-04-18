from tkinter import *
from AccessDatabase import *
from WriteCSV import *


class App:
    def __init__(self):

        self.root = Tk()
        self.root.title("PetIQ Shipping Labels")
        self.root.config(background="darkgray")
        #self.root.geometry('500x500')

        self.leftFrame = Frame(self.root, width=2000, height=1000)
        self.leftFrame.grid(row=0, column=0, padx=10, pady=2)

        self.leftPanel = LeftPanel(self.root, self.leftFrame)

    def start(self):
        self.root.mainloop()


class LeftPanel():
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.frame.config(background="lightgray")

        Label(self.frame, text="SHP Number:", bg="lightgray").grid(row=0, column=0, padx=10, pady=2)

        self.instruct = Entry(self.frame)
        self.instruct.grid(row=0, column=1, padx=10, pady=2)

        Label(self.frame, text="2nd SHP Number (optional):", bg="lightgray").grid(row=1, column=0, padx=10, pady=2)

        self.instruct2 = Entry(self.frame)
        self.instruct2.grid(row=1, column=1, padx=10, pady=2)

        Label(self.frame, text="3rd SHP Number (optional:", bg="lightgray").grid(row=2, column=0, padx=10, pady=2)

        self.instruct3 = Entry(self.frame)
        self.instruct3.grid(row=2, column=1, padx=10, pady=2)

        # Boxes
        Label(self.frame, text="# of Boxes:", bg="lightgray").grid(row=3, column=0, padx=10, pady=2)
        bchoices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        self.bvar = StringVar()
        self.bvar.set(bchoices[0])

        self.boxes = OptionMenu(self.frame, self.bvar, *bchoices)
        self.boxes.grid(row=3, column=1, padx=10, pady=2)

        # Pallets
        Label(self.frame, text="# of Pallets:", bg="lightgray").grid(row=4, column=0, padx=10, pady=2)
        pchoices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        self.pvar = StringVar()
        self.pvar.set(bchoices[0])

        self.pallets = OptionMenu(self.frame, self.pvar, *pchoices)
        self.pallets.grid(row=4, column=1, padx=10, pady=2)

        # Freight
        Label(self.frame, text="# of Freight:", bg="lightgray").grid(row=5, column=0, padx=10, pady=2)
        fchoices = [0, 1, 2, 3, 4, 5]

        self.fvar = StringVar()
        self.fvar.set(bchoices[0])

        self.freight = OptionMenu(self.frame, self.fvar, *fchoices)
        self.freight.grid(row=5, column=1, padx=10, pady=2)

        self.btnFrame = Frame(self.frame, width=200, height=10, padx=10, pady=2, bg="lightgray")
        self.btnFrame.grid(row=1, column=2, padx=10, pady=2)

        self.goBtn = Button(self.btnFrame, text="Go Button!", command=self.get_shp)
        self.goBtn.grid(row=0, column=1, padx=10, pady=2)

    def get_shp(self):
        get = AccessDatabase(self.instruct.get())
        shp2 = self.instruct2.get()
        shp3 = self.instruct3.get()
        labels = [self.bvar.get(), self.pvar.get(), self.fvar.get()]
        tag, repeat = '', 0

        if int(labels[0]) != 0:
            repeat = int(labels[0])
            tag = 'Box'
        if int(labels[1]) != 0:
            repeat = int(labels[1])
            tag = 'Pallet'
        if int(labels[2]) != 0:
            repeat = int(labels[2])
            tag = 'Freight'

        get.get_data()
        data = [get.shp_number, get.po_number, get.company, tag, shp2, shp3]
        makecsv = WriteCSV()
        makecsv.write(data, repeat)

        #print("GUI.get SHP: " + get.shp_number)
        #print("GUI.get PO: " + get.po_number)
        #print("GUI.get Company: " + get.company)
