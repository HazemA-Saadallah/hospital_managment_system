import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from random import choice
from commonFunctions import *

root = tk.Tk()
root.title("Doctor Screen")
root.wm_state("normal")
root.columnconfigure((0), weight=1)
root.rowconfigure((0), weight=1)
masterFrame = tk.Frame(root)
masterFrame.rowconfigure((0, 1, 2), weight=1)
masterFrame.columnconfigure((0), weight=1)
masterFrame.grid(column=0, row=0, sticky="nsew")

# global variables
welcomeFont = ("Meiryo UI", 36, "bold")
submessageFont = ("meiryo ui", 18)
logoutFont = ("Meiryo UI", 12, "bold")
patientFont = ("Meiryo UI", 36, "bold")
tableFontHeading = ("Lucidia Sans", 17, "bold")
tableFont = ("Lucidia Sans", 12)

sources = ["Hospital", "Reception", "Transfer", "Hospital Transfer"]
firstNames = ["John", "Tom", "Jones", "Mohamed", "Cliff", "Arriana", "Melissa"]
lastNames = ["Thomas", "Sombol", "Hambola", "Mohsen", "Alshishi", "AlFerdesy", "Dynamite"]
date = "XX/YY/ZZ"

# Note: The logoutframe is a child of the welcome frame

# Welcome screen section
profilePictureImage = loadImage("./assets/noPersonBorderless.png", 180, 180)
welcomeFrame = tk.Frame(masterFrame)
welcomeFrame.grid(column=0, row=0, sticky="nsew")
welcomeFrame.columnconfigure((0, 1, 2), weight=1)
welcomeFrame.rowconfigure((0, 1), weight=1)
welcomeMessage = "Welcome Dr. Bassem Mohamed Elsaadany!"
patientsMessage = "You have a total of 19 patients for today."
welcomeLabel = tk.Label(welcomeFrame, text=welcomeMessage, font=welcomeFont, anchor="sw")
patientsLabel = tk.Label(welcomeFrame, text=patientsMessage, font=submessageFont, anchor="nw")
pictureLabel = tk.Label(welcomeFrame, image=profilePictureImage)
welcomeLabel.grid(column=1, row=0, padx=20,  sticky="nsw")
patientsLabel.grid(column=1, row=1, padx=20, sticky="nsew")
pictureLabel.grid(column=0, row=0, rowspan=2, padx=20, sticky="nsew")

# logout picture mini section
logoutImage = loadImage("./assets/logout.png", 50, 50)
logoutFrame = tk.Frame(welcomeFrame)
logoutFrame.rowconfigure((0, 1), weight=1)
logoutFrame.columnconfigure((0), weight=1)
logoutFrame.grid(column=2, row=0, sticky="ew", columnspan=1)
logoutImageButton = tk.Button(logoutFrame, image=logoutImage, anchor="e")
logoutImageButton.grid(row=0, column=0, padx=20, pady=2, sticky="ne")
logoutText = tk.Label(logoutFrame, text="Log out?", font=logoutFont, anchor="e")
logoutText.grid(column=0, row=1, padx=10, sticky="e")

# table section (with title)
tableFrame = tk.Frame(masterFrame)
tableFrame.grid(column=0, row=1, sticky="nsew")
tableFrame.rowconfigure((0, 1, 2), weight=1)
tableFrame.columnconfigure((0, 1, 2, 3, 4), weight=1)
patientTitle = tk.Label(tableFrame, text="Patients List", font=patientFont, anchor="n")
patientTitle.grid(row=0, column=0, padx=20, sticky="n", columnspan=5)
# table itself
ttkStyle = ttk.Style()
ttkStyle.configure("Treeview", font=tableFont)
ttkStyle.configure("Treeview.Heading", font=tableFontHeading)
table = ttk.Treeview(tableFrame, columns=('id', 'name', 'date', 'record'), show="headings", height=20)
table.heading(('id'), text="Patient ID")
table.heading(('name'), text="Full Name")
table.heading(('date'), text="Appointment Time")
table.heading(('record'), text="Medical Record")
verticalScrollBar = ttk.Scrollbar(root, orient="vertical", command=table.yview)
table.configure(yscrollcommand=verticalScrollBar.set)
table.grid(row=1, column=0, padx=15, sticky="nsew", columnspan=5, rowspan=1)

for i in range(30):
    firstName = choice(firstNames)
    lastName = choice(lastNames)
    reason = choice(sources)
    fullName = firstName + " " + lastName
    record = firstName.lower() + "_" + lastName.lower() + ".xlsx"
    data = (i, fullName, "XX/YY/ZZ XX:YY PM", record)
    table.insert(parent="", index=tk.END, values=data)

buttonNames = ["Remove Patient", "Edit Patient", "Transfer Patient", "View Medical Record", "View Full Information"]

for i in range(len(buttonNames)):
    tempButton = tk.Button(tableFrame, text=buttonNames[i], font=submessageFont, bg="#1ebbd7", anchor="center")
    tempButton.grid(column=i, row=2, sticky="nsew", padx=15, pady=10)

root.mainloop()
