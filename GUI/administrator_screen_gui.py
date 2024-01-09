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


class adminstrator_screen:
    def __init__(self, username: str) -> None:
        self.username = username
        self.HOME_STATE = False
        self.HOME_VAR = []
        self.FINANCIAL_STATE = False
        self.FINANCIAL_VAR = []
        self.USERS_MANAGEMENT_STATE = False
        self.USERS_MANAGEMENT_VAR = []
        self.RECIPTIONIST_STATE = False
        self.RECIPTIONIST_VAR = []
        self.window = tkinter.Tk()
        self.window.title("Admin Screen")
        self.window.wm_state("normal")
        self.window.columnconfigure((0), weight=1)
        self.window.rowconfigure((0), weight=1)
        self.masterframe = tkinter.Frame(self.window)
        self.masterframe.rowconfigure((0), weight=1)
        self.masterframe.columnconfigure((0), weight=1)
        self.masterframe.grid(column=0, row=0, sticky="nsew")

        self.masterMenu = tkinter.Menu(self.window)
        self.window.config(menu=self.masterMenu)
        self.modeMenu = tkinter.Menu(master=self.masterMenu)
        self.masterMenu.add_cascade(label="Mode", menu=self.modeMenu)
        self.modeMenu.add_command(label="Home", command=self.goToHome)
        self.modeMenu.add_separator()
        self.modeMenu.add_command(label="Financial Management", command=self.goToFinancial)
        self.modeMenu.add_separator()
        self.modeMenu.add_command(label="Reciption Management", command=self.goToReciptionist)
        self.modeMenu.add_separator()
        self.modeMenu.add_command(label="Users Management", command=self.goToUserManagment)

        self.createHome()

    def createHome(self):
        if not self.HOME_STATE:
            self.home_frame = tkinter.Frame(master=self.masterframe)
            self.home_frame.rowconfigure((0, 1, 2), weight=1)
            self.home_frame.columnconfigure((0), weight=1)
            self.home_frame.grid(row=0, column=0, sticky="nsew")

            self.profilePictureImage = Image.open("GUI/assets/noPersonBorderless.png")
            self.profilePictureImage = self.profilePictureImage.resize((280, 280), Image.Resampling.LANCZOS)
            self.profilePictureImage = ImageTk.PhotoImage(self.profilePictureImage)
            pictureLabel = tkinter.Label(master=self.home_frame, image=self.profilePictureImage, anchor="s")
            welcomeMessage = "Welcome " + self.username
            subWelcomeMessage = "Please select a mode to continue from the system menu"
            textLabel = tkinter.Label(master=self.home_frame, text=welcomeMessage, anchor="n", font=("Meiryo UI", 40, "bold"))
            subTextLabel = tkinter.Label(master=self.home_frame, text=subWelcomeMessage, anchor="n", font=("Meiryo UI", 18))
            pictureLabel.grid(row=0, column=0, padx=10, sticky="s")
            textLabel.grid(row=1, column=0, padx=10, sticky="ew")
            subTextLabel.grid(row=2, column=0, padx=10, sticky="n")
            self.HOME_VAR.append(self.home_frame)
            self.HOME_STATE = True

    def create_reciptionist(self):
        if not self.RECIPTIONIST_STATE:
            self.reciptionist_frame = tkinter.Frame(self.masterframe)
            self.reciptionist_frame.rowconfigure((0, 1, 2), weight=1)
            self.reciptionist_frame.columnconfigure((0), weight=1)
            self.reciptionist_frame.grid(column=0, row=0, sticky="nsew")

            user_data_section = tkinter.Frame(self.reciptionist_frame)
            user_data_section.grid(column=0, row=0, sticky="nsew")
            user_data_section.columnconfigure((0, 1, 2), weight=1)
            user_data_section.rowconfigure((0, 1), weight=1)
            welcomeMessage = "Welcome "+self.username
            patientsMessage = "There are currently XYZ appointments"
            welcomeLabel = tkinter.Label(user_data_section, text=welcomeMessage, font=("Meiryo UI", 36, "bold"), anchor="sw")
            patientsLabel = tkinter.Label(user_data_section, text=patientsMessage, font=("Meiryo UI", 18), anchor="nw")
            self.profilePictureImage = Image.open("GUI/assets/noPersonBorderless.png")
            self.profilePictureImage = self.profilePictureImage.resize((280, 280), Image.Resampling.LANCZOS)
            self.profilePictureImage = ImageTk.PhotoImage(self.profilePictureImage)
            pictureLabel = tkinter.Label(user_data_section, image=self.profilePictureImage)
            welcomeLabel.grid(column=1, row=0, padx=20,  sticky="nsw")
            patientsLabel.grid(column=1, row=1, padx=20, sticky="nsew")
            pictureLabel.grid(column=0, row=0, rowspan=2, padx=20, sticky="nsew")

            logoutFrame = tkinter.Frame(user_data_section)
            logoutFrame.rowconfigure((0, 1), weight=1)
            logoutFrame.columnconfigure((0), weight=1)
            logoutFrame.grid(column=2, row=0, sticky="ew", columnspan=1)
            self.logoutImage = Image.open("GUI/assets/logout.png")
            self.logoutImage = self.logoutImage.resize((50, 50), Image.Resampling.LANCZOS)
            self.logoutImage = ImageTk.PhotoImage(self.logoutImage)
            logoutImageButton = tkinter.Button(logoutFrame, image=self.logoutImage, anchor="e")
            logoutImageButton.grid(row=0, column=0, padx=20, pady=2, sticky="ne")
            logoutText = tkinter.Label(logoutFrame, text="Log out?", font=("Meiryo UI", 12, "bold"), anchor="e")
            logoutText.grid(column=0, row=1, padx=10, sticky="e")

            tableFrame = tkinter.Frame(self.reciptionist_frame)
            tableFrame.grid(column=0, row=1, sticky="nsew")
            tableFrame.rowconfigure((0, 1, 2), weight=1)
            tableFrame.columnconfigure((0, 1, 2, 3), weight=1)
            patientTitle = tkinter.Label(tableFrame, text="Appointments List", font=("Meiryo UI", 36, "bold"), anchor="n")
            patientTitle.grid(row=0, column=0, padx=20, sticky="n", columnspan=4)

            ttkStyle = ttk.Style()
            ttkStyle.configure("Treeview", font=("Lucidia Sans", 12))
            ttkStyle.configure("Treeview.Heading", font=("Lucidia Sans", 17, "bold"))
            table = ttk.Treeview(tableFrame, columns=('pname', 'dname', 'spec', 'date'), show="headings", height=20)
            table.heading(('pname'), text="Patient Name")
            table.heading(('dname'), text="Doctor Name")
            table.heading(('spec'), text="Specialization")
            table.heading(('date'), text="Appointment Date")
            verticalScrollBar = ttk.Scrollbar(self.window, orient="vertical", command=table.yview)
            table.configure(yscrollcommand=verticalScrollBar.set)
            table.grid(row=1, column=0, padx=15, sticky="nsew", columnspan=4, rowspan=1)
            buttonNames = ["Register Patient", "Create Appointment", "Edit Appointment", "Cancel Appointment"]

            for i in range(len(buttonNames)):
                tempButton = tkinter.Button(tableFrame, text=buttonNames[i], font=("Meiryo UI", 18), bg="#1ebbd7", anchor="center")
                tempButton.grid(column=i, row=2, sticky="nsew", padx=15, pady=10)
            self.RECIPTIONIST_VAR.append(self.reciptionist_frame)
            self.RECIPTIONIST_STATE = True

    def create_financial(self):
        if not self.FINANCIAL_STATE:
            self.financialFrame = tkinter.Frame(master=self.masterframe)
            self.financialFrame.rowconfigure((0, 1, 2, 3, 4), weight=1)
            self.financialFrame.columnconfigure((0), weight=1)
            self.financialFrame.grid(column=0, row=0, sticky="nsew")
            self.finTitleLabel = tkinter.Label(master=self.financialFrame, text="Financial Management", anchor="center", font=("Meiryo UI", 36, "bold"))
            self.finTitleLabel.grid(row=0, column=0, sticky="ew")
            finTable = ttk.Treeview(self.financialFrame, show="headings", columns=("transName", "transID", "cashIn", "cashOut"))
            finTable.heading(("transName"), text="Transaction Name")
            finTable.heading(("transID"), text="Transaction ID")
            finTable.heading(("cashIn"), text="Cash In")
            finTable.heading(("cashOut"), text="Cash Out")
            finTable.grid(row=1, rowspan=3, column=0, sticky="nsew")

            cashFlows = ["Revenue: XXXX", "Expenses: YYYY", "Profit: ZZZZ"]
            cashFlowsFrame = tkinter.Frame(self.financialFrame)
            cashFlowsFrame.rowconfigure((0), weight=1)
            cashFlowsFrame.columnconfigure((0, 1, 2), weight=1)
            cashFlowsFrame.grid(row=4, column=0, sticky="nsew")
            for i in range(len(cashFlows)):
                cashFlowButton = tkinter.Label(master=cashFlowsFrame, text=cashFlows[i], anchor="center", font=("Meiryo UI", 24, "bold"))
                cashFlowButton.grid(column=i, row=0, sticky="ew", padx=15)
            self.FINANCIAL_VAR.append(self.financialFrame)
            self.FINANCIAL_STATE = True

    def User_management(self):
        if not self.USERS_MANAGEMENT_STATE:
            self.user_management_frame = tkinter.Frame(self.masterframe)
            self.user_management_frame.rowconfigure((0, 1, 2), weight=1)
            self.user_management_frame.columnconfigure((0), weight=1)
            self.user_management_frame.grid(column=0, row=0, sticky="nsew")

            self.profilePictureImage = Image.open("GUI/assets/noPersonBorderless.png")
            self.profilePictureImage = self.profilePictureImage.resize((180, 180), Image.Resampling.LANCZOS)
            self.profilePictureImage = ImageTk.PhotoImage(self.profilePictureImage)
            user_data_frame = tkinter.Frame(self.user_management_frame)
            user_data_frame.grid(column=0, row=0, sticky="nsew")
            user_data_frame.columnconfigure((0, 1, 2), weight=1)
            user_data_frame.rowconfigure((0, 1), weight=1)
            welcomeMessage = "Welcome " + self.username
            patientsMessage = "You have a total of 19 patients for today."
            welcomeLabel = tkinter.Label(user_data_frame, text=welcomeMessage, font=("Meiryo UI", 36, "bold"), anchor="sw")
            patientsLabel = tkinter.Label(user_data_frame, text=patientsMessage, font=("Meiryo UI", 36, "bold"), anchor="nw")
            pictureLabel = tkinter.Label(user_data_frame, image=self.profilePictureImage)
            welcomeLabel.grid(column=1, row=0, padx=20,  sticky="nsw")
            patientsLabel.grid(column=1, row=1, padx=20, sticky="nsew")
            pictureLabel.grid(column=0, row=0, rowspan=2, padx=20, sticky="nsew")

            self.logoutImage = Image.open("GUI/assets/logout.png")
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

            self.tableFrame = tkinter.Frame(self.user_management_frame)
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

            firstNames = ["John", "Tom", "Jones", "Mohamed", "Cliff", "Arriana", "Melissa"]
            lastNames = ["Thomas", "Sombol", "Hambola", "Mohsen", "Alshishi", "AlFerdesy", "Dynamite"]
            for i in range(50):
                firstName = random.choice(firstNames)
                lastName = random.choice(lastNames)
                fullName = firstName + " " + lastName
                record = firstName.lower() + "_" + lastName.lower() + ".xlsx"
                data = (i, fullName, "XX/YY/ZZ XX:YY PM", record)
                self.table.insert(parent="", index=tkinter.END, values=data)
            self.USERS_MANAGEMENT_VAR.append(self.user_management_frame)
            self.USERS_MANAGEMENT_STATE = True

    def goToHome(self):
        self.destroyUserManagement()
        self.destroyReciptionist()
        self.destroyFinancial()
        self.createHome()

    def goToFinancial(self):
        self.destroyHome()
        self.destroyReciptionist()
        self.destroyUserManagement()
        self.create_financial()

    def goToUserManagment(self):
        self.destroyHome()
        self.destroyFinancial()
        self.destroyReciptionist()
        self.User_management()

    def goToReciptionist(self):
        self.destroyHome()
        self.destroyFinancial()
        self.destroyUserManagement()
        self.create_reciptionist()

    def destroyHome(self):
        if self.HOME_STATE:
            for obj in self.HOME_VAR:
                obj.destroy()
            self.HOME_STATE = False

    def destroyFinancial(self):
        if self.FINANCIAL_STATE:
            for obj in self.FINANCIAL_VAR:
                obj.destroy()
            self.FINANCIAL_STATE = False

    def destroyReciptionist(self):
        if self.RECIPTIONIST_STATE:
            for obj in self.RECIPTIONIST_VAR:
                obj.destroy()
            self.RECIPTIONIST_STATE = False

    def destroyUserManagement(self):
        if self.USERS_MANAGEMENT_STATE:
            for obj in self.USERS_MANAGEMENT_VAR:
                obj.destroy()
            self.USERS_MANAGEMENT_STATE = False

    def run(self):
        self.window.mainloop()
