import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
import random

import importlib.util
import sys

spec = importlib.util.spec_from_file_location("login_lookup", "DataBase/login_lookup.py")
login_lookup = importlib.util.module_from_spec(spec)
sys.modules["login_lookup"] = login_lookup
spec.loader.exec_module(login_lookup)


class doctor_screen:
    def __init__(self, username: str) -> None:
        self.username = username
        self.window = tkinter.Tk()
        self.window.title("Doctor Screen")
        self.window.wm_state("normal")
        self.window.columnconfigure((0), weight=1)
        self.window.rowconfigure((0), weight=1)
        self.masterframe = tkinter.Frame(self.window)
        self.masterframe.rowconfigure((0, 1, 2), weight=1)
        self.masterframe.columnconfigure((0), weight=1)
        self.masterframe.grid(column=0, row=0, sticky="nsew")
        self.profilePictureImage = Image.open("GUI/assets/noPersonBorderless.png")
        self.logoutImage = Image.open("GUI/assets/logout.png")

        self.init_user_data_section()
        self.init_table()
        self.table_inser_dumy_data()

    def init_user_data_section(self):
        self.profilePictureImage = self.profilePictureImage.resize((180, 180), Image.Resampling.LANCZOS)
        self.profilePictureImage = ImageTk.PhotoImage(self.profilePictureImage)
        user_data_frame = tkinter.Frame(self.masterframe)
        user_data_frame.grid(column=0, row=0, sticky="nsew")
        user_data_frame.columnconfigure((0, 1, 2), weight=1)
        user_data_frame.rowconfigure((0, 1), weight=1)
        welcomeMessage = "Welcome Dr. " + self.username
        patientsMessage = "You have a total of 19 patients for today."
        welcomeLabel = tkinter.Label(user_data_frame, text=welcomeMessage, font=("Meiryo UI", 36, "bold"), anchor="sw")
        patientsLabel = tkinter.Label(user_data_frame, text=patientsMessage, font=("Meiryo UI", 36, "bold"), anchor="nw")
        pictureLabel = tkinter.Label(user_data_frame, image=self.profilePictureImage)
        welcomeLabel.grid(column=1, row=0, padx=20,  sticky="nsw")
        patientsLabel.grid(column=1, row=1, padx=20, sticky="nsew")
        pictureLabel.grid(column=0, row=0, rowspan=2, padx=20, sticky="nsew")

        self.logoutImage = self.logoutImage.resize((50, 50), Image.Resampling.LANCZOS)
        self.logoutImage = ImageTk.PhotoImage(self.logoutImage)
        logoutFrame = tkinter.Frame(user_data_frame)
        logoutFrame.rowconfigure((0, 1), weight=1)
        logoutFrame.columnconfigure((0), weight=1)
        logoutFrame.grid(column=2, row=0, sticky="ew", columnspan=1)
        logoutImageButton = tkinter.Button(logoutFrame, image=self.logoutImage, anchor="e")
        logoutImageButton.grid(row=0, column=0, padx=20, pady=2, sticky="ne")
        logoutText = tkinter.Label(logoutFrame, text="Log out?", font=("Meiryo UI", 12, "bold"), anchor="e")
        logoutText.grid(column=0, row=1, padx=10, sticky="e")

    def init_table(self):
        self.tableFrame = tkinter.Frame(self.masterframe)
        self.tableFrame.grid(column=0, row=1, sticky="nsew")
        self.tableFrame.rowconfigure((0, 1, 2), weight=1)
        self.tableFrame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        patientTitle = tkinter.Label(self.tableFrame, text="Patients List", font=("Meiryo UI", 36, "bold"), anchor="n")
        patientTitle.grid(row=0, column=0, padx=20, sticky="n", columnspan=5)

        ttkStyle = ttk.Style()
        ttkStyle.configure("Treeview", font=("Lucidia Sans", 15), rowheight=50)
        ttkStyle.configure("Treeview.Heading", font=("Lucidia Sans", 17, "bold"))
        self.table = ttk.Treeview(self.tableFrame, columns=('id', 'name', 'date', 'record'), show="headings", height=10)
        self.table.heading(('id'), text="Patient ID")
        self.table.heading(('name'), text="Full Name")
        self.table.heading(('date'), text="Appointment Time")
        self.table.heading(('record'), text="Medical Record")
        verticalScrollBar = ttk.Scrollbar(self.window, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=verticalScrollBar.set)
        self.table.grid(row=1, column=0, padx=15, sticky="nsew", columnspan=5, rowspan=1)

        buttonNames = ["Remove Patient", "Edit Patient", "Transfer Patient", "View Medical Record", "View Full Information"]

        for i in range(len(buttonNames)):
            tempButton = tkinter.Button(self.tableFrame, text=buttonNames[i], font=("meiryo ui", 18), bg="#1ebbd7", anchor="center")
            tempButton.grid(column=i, row=2, sticky="nsew", padx=15, pady=10)

    def table_inser_dumy_data(self):
        firstNames = ["John", "Tom", "Jones", "Mohamed", "Cliff", "Arriana", "Melissa"]
        lastNames = ["Thomas", "Sombol", "Hambola", "Mohsen", "Alshishi", "AlFerdesy", "Dynamite"]
        for i in range(50):
            firstName = random.choice(firstNames)
            lastName = random.choice(lastNames)
            fullName = firstName + " " + lastName
            record = firstName.lower() + "_" + lastName.lower() + ".xlsx"
            data = (i, fullName, "XX/YY/ZZ XX:YY PM", record)
            self.table.insert(parent="", index=tkinter.END, values=data)

    def run(self):
        self.window.mainloop()
