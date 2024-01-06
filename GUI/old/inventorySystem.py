import tkinter as tk
from tkinter import ttk
from commonFunctions import *

#initialization
root = tk.Tk()
root.wm_state("zoomed")
root.title("Inventory System")
root.columnconfigure((0),weight=1)
root.rowconfigure((0),weight=1)
masterFrame = tk.Frame(root)
masterFrame.rowconfigure((0,1,2),weight=1)
masterFrame.columnconfigure((0),weight=1)
masterFrame.grid(row=0,column=0,sticky="nsew")

#global variables section
titleFont = ("Segoe UI", 38, "bold")
logoutFont = ("Meiryo UI", 12, "bold")
buttonFont = ("Meiryo UI", 18)
logoutPicture = loadImage("./assets/logout.png", 60,60)

#title section
titleFrame = tk.Frame(masterFrame)
titleFrame.rowconfigure((0,1),weight=1)
titleFrame.columnconfigure((0),weight=3)
titleFrame.columnconfigure((1),weight=1)
titleFrame.grid(row=0,column=0, sticky="new")
titleLabel = tk.Label(master=titleFrame, font=titleFont, anchor="center",text="Inventory Management Subsystem")
logoutImageLabel = tk.Button(master=titleFrame,image=logoutPicture, anchor="e")
logoutTextLabel = tk.Label(master=titleFrame,text="Log Out?", font=logoutFont, anchor="ne")
titleLabel.grid(row=0,column=0,padx=20,pady=5, sticky="nsew")
logoutImageLabel.grid(row=0,column=1, padx=20, pady=15, sticky="ne")
logoutTextLabel.grid(row=1,column=1,sticky="ne",padx=20)

#table section
table = ttk.Treeview(master=masterFrame, height=25, show="headings", columns=("id","name","dose","quantity","threshold","resupply","withdrawal"))
table.heading(('id'),text="Item ID")
table.heading(('name'), text="Item Name")
table.heading(('dose'), text="Item Dose")
table.heading(("quantity"),text="Item Quantity")
table.heading(("threshold"), text="Minimum Supply")
table.heading(("resupply"), text="Last Resupply")
table.heading(("withdrawal"),text="Last Withdrawal")
table.grid(row=1,column=0, sticky="nsew",padx=20,pady=15)

actions = ["Add Item", "Remove Item", "Edit Item"]
buttonFrame = tk.Frame(master=masterFrame)
buttonFrame.grid(column=0,row=2, columnspan=4, sticky="nsew")
buttonFrame.columnconfigure((0,1,2),weight=1)
buttonFrame.rowconfigure((0),weight=1)
for i in range(len(actions)):
    tempButton = tk.Button(master=buttonFrame, text=actions[i], font=buttonFont,bg="#1ebbd7",anchor="center")
    tempButton.grid(column=i, row=2, padx=20, pady=10, sticky="nsew")
root.mainloop()