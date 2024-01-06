import tkinter as tk
from tkinter import ttk
from commonFunctions import *

#intialization
root = tk.Tk()
root.title("Receptionist Screen")
root.wm_state("zoomed")
root.columnconfigure((0),weight=1)
root.rowconfigure((0),weight=1)
masterFrame = tk.Frame(root)
masterFrame.rowconfigure((0,1,2), weight=1)
masterFrame.columnconfigure((0),weight=1)
masterFrame.grid(column=0,row=0,sticky="nsew")

#global variables
welcomeFont = ("Meiryo UI", 36, "bold")
submessageFont = ("Meiryo UI", 18)
logoutFont = ("Meiryo UI", 12, "bold")
patientFont = ("Meiryo UI", 36, "bold")
tableFontHeading = ("Lucidia Sans", 17,"bold")
tableFont = ("Lucidia Sans", 12)

#Welcome screen section
profilePictureImage = loadImage("./assets/noPersonBorderless.png", 180, 180)
welcomeFrame = tk.Frame(masterFrame)
welcomeFrame.grid(column=0, row=0,sticky="nsew")
welcomeFrame.columnconfigure((0,1,2),weight=1)
welcomeFrame.rowconfigure((0,1),weight=1)
welcomeMessage = "Welcome Sara Mohamed Elbassiouny!"
patientsMessage = "There are currently XYZ appointments"
welcomeLabel = tk.Label(welcomeFrame, text=welcomeMessage, font=welcomeFont,anchor="sw")
patientsLabel = tk.Label(welcomeFrame, text=patientsMessage, font=submessageFont,anchor="nw")
pictureLabel = tk.Label(welcomeFrame, image=profilePictureImage)
welcomeLabel.grid(column=1, row=0, padx=20,  sticky="nsw")
patientsLabel.grid(column=1, row=1, padx=20, sticky="nsew")
pictureLabel.grid(column=0, row=0, rowspan=2, padx=20, sticky="nsew")

#logout picture mini section
logoutImage = loadImage("./assets/logout.png",50,50)
logoutFrame = tk.Frame(welcomeFrame)
logoutFrame.rowconfigure((0,1),weight=1)
logoutFrame.columnconfigure((0),weight=1)
logoutFrame.grid(column=2,row=0,sticky="ew",columnspan=1)
logoutImageButton = tk.Button(logoutFrame, image=logoutImage, anchor="e")
logoutImageButton.grid(row=0,column=0, padx=20,pady=2, sticky="ne")
logoutText = tk.Label(logoutFrame, text="Log out?", font=logoutFont, anchor="e")
logoutText.grid(column=0,row=1,padx=10,sticky="e")

#table section (with title)
tableFrame = tk.Frame(masterFrame)
tableFrame.grid(column=0, row=1,sticky="nsew")
tableFrame.rowconfigure((0,1,2),weight=1)
tableFrame.columnconfigure((0,1,2,3),weight=1)
patientTitle = tk.Label(tableFrame, text="Appointments List", font=patientFont,anchor="n")
patientTitle.grid(row=0,column=0, padx=20,sticky="n",columnspan=4)
#table itself
ttkStyle = ttk.Style()
ttkStyle.configure("Treeview",font=tableFont)
ttkStyle.configure("Treeview.Heading",font=tableFontHeading)
table = ttk.Treeview(tableFrame, columns=('pname','dname', 'spec','date'), show="headings", height=20)
table.heading(('pname'), text="Patient Name")
table.heading(('dname'), text="Doctor Name")
table.heading(('spec'), text="Specialization")
table.heading(('date'), text="Appointment Date")
verticalScrollBar = ttk.Scrollbar(root, orient="vertical", command=table.yview)
table.configure(yscrollcommand=verticalScrollBar.set)
table.grid(row=1,column=0,padx=15, sticky="nsew",columnspan=4, rowspan=1)

buttonNames = ["Register Patient", "Create Appointment", "Edit Appointment", "Cancel Appointment"]

for i in range(len(buttonNames)):
    tempButton = tk.Button(tableFrame, text=buttonNames[i], font=submessageFont, bg="#1ebbd7",anchor="center")
    tempButton.grid(column=i, row=2,sticky="nsew",padx=15,pady=10)

root.mainloop()