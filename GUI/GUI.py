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


class login_screen:
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Login")
        self.window.resizable(False, False)
        self.masterframe = tkinter.Frame(self.window)
        self.masterframe.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.masterframe.columnconfigure((0), weight=1)
        self.masterframe.grid(column=0, row=0, sticky="ew")
        self.logo = Image.open("GUI/assets/hospitalLogo.png")

        self.init_logo()
        self.init_login_massage()
        self.init_username_section()
        self.init_password_section()
        self.init_button_section()

    def init_logo(self):
        self.logo_frame = tkinter.Frame(self.masterframe)
        self.logo_frame.grid(row=0, column=0, sticky="ew", pady=10)
        self.logo_frame.rowconfigure((0), weight=1)
        self.logo_frame.columnconfigure((0, 1), weight=1)

        self.logo_label = tkinter.Label(self.logo_frame, text="F-JUST", font=("Meiryo UI", 24, "bold"), anchor="w")
        self.logo_label.grid(row=0, column=1, sticky="nsew")

        self.logo = self.logo.resize((65, 65), Image.Resampling.LANCZOS)
        self.companyLogoImage = ImageTk.PhotoImage(self.logo)
        companyImageLabel = tkinter.Label(self.logo_frame, image=self.companyLogoImage, anchor="e")
        companyImageLabel.grid(column=0, row=0, sticky="nsew")

    def init_login_massage(self):
        self.massage_frame = tkinter.Frame(self.masterframe)
        self.massage_frame.grid(row=1, column=0, pady=10, padx=10)
        self.massage_frame.rowconfigure((0, 1), weight=1)
        self.massage_frame.columnconfigure((0), weight=1)
        self.loginMessageLabel = tkinter.Label(self.massage_frame, text="Log In:", font=("Arial", 18, "bold"), anchor="w")
        self.loginMessageDescriptionLabel = tkinter.Label(self.massage_frame, text="Please log in with your Employee ID and password", font=("Meiryo UI", 12))
        self.loginMessageLabel.grid(column=0, row=1, sticky="w", padx=10)
        self.loginMessageDescriptionLabel.grid(column=0, row=2, sticky="w", padx=10)

    def init_username_section(self):
        self.username_input_frame = tkinter.Frame(self.masterframe)
        self.username_input_frame.rowconfigure((0, 1, 2), weight=1)
        self.username_input_frame.columnconfigure((0), weight=1)
        self.username_input_frame.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)
        self.username_input_label = tkinter.Label(self.username_input_frame, text="Employee ID: ", anchor="w", font=("Meiryo UI", 14, "bold"))
        self.username_input_box = tkinter.Entry(self.username_input_frame, font=("Meiryo UI", 12))
        self.username_input_label.grid(row=0, column=0, sticky="nsew", pady=3, padx=10)
        self.username_input_box.grid(row=1, column=0, sticky="nsew", padx=10)

        self.wrong_username_label = tkinter.Label(self.username_input_frame, text="Employee ID does not exist!", anchor="w", fg="red", font=("Meiryo UI", 10))

    def init_password_section(self):
        self.passwordIDFrame = tkinter.Frame(self.masterframe)
        self.passwordIDFrame.rowconfigure((0, 1, 2), weight=1)
        self.passwordIDFrame.columnconfigure((0), weight=1)
        self.passwordIDFrame.grid(row=3, column=0, sticky="nsew", pady=10, padx=10)
        self.passwordIDLabel = tkinter.Label(self.passwordIDFrame, text="Password: ", anchor="w", font=("Meiryo UI", 14, "bold"))
        self.passwordIDTextBox = tkinter.Entry(self.passwordIDFrame, font=("Meiryo UI", 12), show="*")
        self.passwordIDLabel.grid(row=0, column=0, sticky="nsew", pady=3, padx=10)
        self.passwordIDTextBox.grid(row=1, column=0, sticky="nsew", padx=10)

        self.wrong_password_label = tkinter.Label(self.passwordIDFrame, text="password is incorrect!", anchor="w", fg="red", font=("Meiryo UI", 10))

    def init_button_section(self):
        self.buttonFrame = tkinter.Frame(self.masterframe)
        self.buttonFrame.rowconfigure((0), weight=1)
        self.buttonFrame.columnconfigure((0), weight=1)
        self.buttonFrame.grid(row=5, column=0, sticky="nsew")
        self.loginButton = tkinter.Button(self.buttonFrame, text="Log In", fg="White", bg="Blue", font=("Meiryo UI", 14, "bold"), anchor="center")
        self.loginButton.grid(column=0, row=0, pady=10, sticky="nsew", padx=10)

    def flag_login_error(self, error_code):
        if error_code == 'username':
            self.wrong_username_label.grid(row=2, column=0, sticky="nsew", padx=10)
        elif error_code == 'password':
            self.wrong_password_label.grid(row=2, column=0, sticky="w", padx=10)
        elif error_code == 'kill_username':
            self.wrong_username_label.grid_forget()
        elif error_code == 'kill_password':
            self.wrong_password_label.grid_forget()

        """ elif error_code == 'both': """
        """     self.wrong_username_label.grid(row=2, column=0, sticky="nsew", padx=10) """
        """     self.wrong_password_label.grid(row=2, column=0, sticky="w", padx=10) """

    def run(self):
        self.window.mainloop()


class reciptionist_screen:
    def __init__(self, username: str) -> None:
        self.username = username
        self.window = tkinter.Tk()
        self.window.title("Receptionist Screen")
        self.window.wm_state("normal")
        self.window.columnconfigure((0), weight=1)
        self.window.rowconfigure((0), weight=1)
        self.masterframe = tkinter.Frame(self.window)
        self.masterframe.rowconfigure((0, 1, 2, 3), weight=1)
        self.masterframe.columnconfigure((0), weight=1)
        self.masterframe.grid(column=0, row=0, sticky="nsew")
        self.profilePictureImage = Image.open("GUI/assets/noPersonBorderless.png")
        self.logoutImage = Image.open("GUI/assets/logout.png")

        self.init_user_data_section()
        self.init_table()

    def init_user_data_section(self):
        self.profilePictureImage = self.profilePictureImage.resize((180, 180), Image.Resampling.LANCZOS)
        self.profilePictureImage = ImageTk.PhotoImage(self.profilePictureImage)
        self.user_data_section = tkinter.Frame(self.masterframe)
        self.user_data_section.grid(column=0, row=0, sticky="nsew")
        self.user_data_section.columnconfigure((0, 1, 2), weight=1)
        self.user_data_section.rowconfigure((0, 1), weight=1)
        self.welcomeMessage = "Welcome " + self.username
        self.patientsMessage = "There are currently XYZ appointments"
        self.welcomeLabel = tkinter.Label(self.user_data_section, text=self.welcomeMessage, font=("Meiryo UI", 36, "bold"), anchor="sw")
        self.patientsLabel = tkinter.Label(self.user_data_section, text=self.patientsMessage, font=("Meiryo UI", 18), anchor="nw")
        self.pictureLabel = tkinter.Label(self.user_data_section, image=self.profilePictureImage)
        self.welcomeLabel.grid(column=1, row=0, padx=20,  sticky="nsw")
        self.patientsLabel.grid(column=1, row=1, padx=20, sticky="nsew")
        self.pictureLabel.grid(column=0, row=0, rowspan=2, padx=20, sticky="nsew")

        self.logoutImage = self.logoutImage.resize((50, 50), Image.Resampling.LANCZOS)
        self.logoutImage = ImageTk.PhotoImage(self.logoutImage)
        self.logoutFrame = tkinter.Frame(self.user_data_section)
        self.logoutFrame.rowconfigure((0, 1), weight=1)
        self.logoutFrame.columnconfigure((0), weight=1)
        self.logoutFrame.grid(column=2, row=0, sticky="ew", columnspan=1)
        self.logoutImageButton = tkinter.Button(self.logoutFrame, image=self.logoutImage, anchor="e")
        self.logoutImageButton.grid(row=0, column=0, padx=20, pady=2, sticky="ne")
        self.logoutText = tkinter.Label(self.logoutFrame, text="Log out?", font=("Meiryo UI", 12, "bold"), anchor="e")
        self.logoutText.grid(column=0, row=1, padx=10, sticky="e")

    def init_table(self):
        self.tableFrame = tkinter.Frame(self.masterframe)
        self.tableFrame.grid(column=0, row=1, sticky="nsew")
        self.tableFrame.rowconfigure((0, 1, 2), weight=1)
        self.tableFrame.columnconfigure((0, 1, 2, 3), weight=1)
        self.patientTitle = tkinter.Label(self.tableFrame, text="Appointments List", font=("Meiryo UI", 36, "bold"), anchor="n")
        self.patientTitle.grid(row=0, column=0, padx=20, sticky="n", columnspan=4)

        self.ttkStyle = ttk.Style()
        self.ttkStyle.configure("Treeview", font=("Lucidia Sans", 12))
        self.ttkStyle.configure("Treeview.Heading", font=("Lucidia Sans", 17, "bold"))
        self.table = ttk.Treeview(self.tableFrame, columns=('pname', 'dname', 'spec', 'date'), show="headings", height=20)
        self.table.heading(('pname'), text="Patient Name")
        self.table.heading(('dname'), text="Doctor Name")
        self.table.heading(('spec'), text="Specialization")
        self.table.heading(('date'), text="Appointment Date")
        self.verticalScrollBar = ttk.Scrollbar(self.window, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.verticalScrollBar.set)
        self.table.grid(row=1, column=0, padx=15, sticky="nsew", columnspan=4, rowspan=1)
        self.buttonNames = ["Register Patient", "Create Appointment", "Edit Appointment", "Cancel Appointment"]

        self.add_patient_frame = tkinter.Frame(self.tableFrame)
        self.add_patient_frame.grid(column=0, row=2, pady=10, sticky="news")
        self.add_patient_frame.rowconfigure((0), weight=1)
        self.add_patient_frame.columnconfigure((0, 1, 2, 3), weight=1)

        self.enter_patient_name = tkinter.Entry(self.add_patient_frame, font=("Meiryo UI", 12))
        self.enter_patient_name.grid(row=0, column=0, padx=20)

        self.opp = ["aa", "bb", "cc", "dd", "ee", "ff", "gg"]
        self.choose_date_list_clicked = tkinter.StringVar()
        self.choose_date_list = tkinter.OptionMenu(self.add_patient_frame, self.choose_date_list_clicked, *self.opp)
        self.choose_date_list.grid(row=0, column=1, padx=20, sticky="news")

        self.enter_patient_name_clicked = tkinter.StringVar()
        self.enter_patient_name = tkinter.OptionMenu(self.add_patient_frame, self.enter_patient_name_clicked, *self.opp)
        self.enter_patient_name.grid(row=0, column=2, padx=20, sticky="news")

        self.choose_doctor_list_clicked = tkinter.StringVar()
        self.choose_doctor_list = tkinter.OptionMenu(self.add_patient_frame, self.choose_doctor_list_clicked, *self.opp)
        self.choose_doctor_list.grid(row=0, column=3, padx=20, sticky="news")

        for i in range(len(self.buttonNames)):
            tempButton = tkinter.Button(self.tableFrame, text=self.buttonNames[i], font=("Meiryo UI", 18), bg="#1ebbd7", anchor="center")
            tempButton.grid(column=i, row=3, sticky="nsew", padx=15, pady=10)

    def run(self):
        self.window.mainloop()


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


class financial_screen:
    def __init__(self, username: str) -> None:
        self.username = username
        self.window = tkinter.Tk()
        self.window.title("Admin Screen")
        self.window.wm_state("normal")
        self.window.columnconfigure((0), weight=1)
        self.window.rowconfigure((0), weight=1)
        self.masterframe = tkinter.Frame(self.window)
        self.masterframe.rowconfigure((0), weight=1)
        self.masterframe.columnconfigure((0), weight=1)
        self.masterframe.grid(column=0, row=0, sticky="nsew")

        self.createFinancial()

    def createFinancial(self):
        financialFrame = tkinter.Frame(master=self.masterframe)
        financialFrame.rowconfigure((0, 1, 2, 3, 4), weight=1)
        financialFrame.columnconfigure((0), weight=1)
        financialFrame.grid(column=0, row=0, sticky="nsew")
        finTitleLabel = tkinter.Label(master=financialFrame, text="Financial Management", anchor="center", font=("Meiryo UI", 36, "bold"))
        finTitleLabel.grid(row=0, column=0, sticky="ew")
        finTable = ttk.Treeview(financialFrame, show="headings", columns=("transName", "transID", "cashIn", "cashOut"))
        finTable.heading(("transName"), text="Transaction Name")
        finTable.heading(("transID"), text="Transaction ID")
        finTable.heading(("cashIn"), text="Cash In")
        finTable.heading(("cashOut"), text="Cash Out")
        finTable.grid(row=1, rowspan=3, column=0, sticky="nsew")

        cashFlows = ["Revenue: XXXX", "Expenses: YYYY", "Profit: ZZZZ"]
        cashFlowsFrame = tkinter.Frame(financialFrame)
        cashFlowsFrame.rowconfigure((0), weight=1)
        cashFlowsFrame.columnconfigure((0, 1, 2), weight=1)
        cashFlowsFrame.grid(row=4, column=0, sticky="nsew")
        for i in range(len(cashFlows)):
            cashFlowButton = tkinter.Label(master=cashFlowsFrame, text=cashFlows[i], anchor="center", font=("Meiryo UI", 24, "bold"))
            cashFlowButton.grid(column=i, row=0, sticky="ew", padx=15)

    def run(self):
        self.window.mainloop()


class administrator_screen:
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


if __name__ == "__main__":
    """ login = login_screen() """
    """ login.run() """

    """ reciptionist = reciptionist_screen("user") """
    """ reciptionist.run() """
    """"""
    doctor = doctor_screen("aa")
    doctor.run()
    """"""
    """ finance = financial_screen() """
    """ finance.run() """
    """"""
    """ admin = adminstrator_screen() """
    """ admin.run() """
