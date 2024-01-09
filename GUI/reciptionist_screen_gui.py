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
        self.tableFrame.columnconfigure((0, 1, 2), weight=1)
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

        self.buttonNames = ["Create Appointment", "Edit Appointment", "Cancel Appointment"]


        for i in range(len(self.buttonNames)):
            tempButton = tkinter.Button(self.tableFrame, text=self.buttonNames[i], font=("Meiryo UI", 18), bg="#1ebbd7", anchor="center")
            tempButton.grid(column=i, row=3, sticky="nsew", padx=15, pady=10)

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

    """ def init_table(self): """
    """     self.tableFrame = tkinter.Frame(self.masterframe) """
    """     self.tableFrame.grid(column=0, row=1, sticky="nsew") """
    """     self.tableFrame.rowconfigure((0, 1, 2), weight=1) """
    """     self.tableFrame.columnconfigure((0, 1, 2), weight=1) """
    """     self.patientTitle = tkinter.Label(self.tableFrame, text="Appointments List", font=("Meiryo UI", 36, "bold"), anchor="n") """
    """     self.patientTitle.grid(row=0, column=0, padx=20, sticky="n", columnspan=4) """
    """"""
    """     self.ttkStyle = ttk.Style() """
    """     self.ttkStyle.configure("Treeview", font=("Lucidia Sans", 12)) """
    """     self.ttkStyle.configure("Treeview.Heading", font=("Lucidia Sans", 17, "bold")) """
    """     self.table = ttk.Treeview(self.tableFrame, columns=('pname', 'dname', 'spec', 'date'), show="headings", height=20) """
    """     self.table.heading(('pname'), text="Patient Name") """
    """     self.table.heading(('dname'), text="Doctor Name") """
    """     self.table.heading(('spec'), text="Specialization") """
    """     self.table.heading(('date'), text="Appointment Date") """
    """     self.verticalScrollBar = ttk.Scrollbar(self.window, orient="vertical", command=self.table.yview) """
    """     self.table.configure(yscrollcommand=self.verticalScrollBar.set) """
    """     self.table.grid(row=1, column=0, padx=15, sticky="nsew", columnspan=4, rowspan=1) """
    """     self.buttonNames = ["Create Appointment", "Edit Appointment", "Cancel Appointment"] """
    """"""
    """     self.add_patient_frame = tkinter.Frame(self.tableFrame) """
    """     self.add_patient_frame.grid(column=0, row=2, pady=10, sticky="news") """
    """     self.add_patient_frame.rowconfigure((0), weight=1) """
    """     self.add_patient_frame.columnconfigure((0, 1, 2, 3, 4), weight=1) """
    """"""
    """     self.enter_patient_name = tkinter.Entry(self.add_patient_frame, font=("Meiryo UI", 12)) """
    """     self.enter_patient_name.grid(row=0, column=0, padx=20) """
    """"""
    """     self.opp = ["aa", "bb", "cc", "dd", "ee", "ff", "gg"] """
    """"""
    """     self.enter_patient_id = tkinter.Entry(self.add_patient_frame, font=("Meiryo UI", 12)) """
    """     self.enter_patient_id.grid(row=0, column=1, padx=20) """
    """"""
    """     self.choose_date_list_clicked = tkinter.StringVar() """
    """     self.choose_date_list_clicked.set("choose a date") """
    """     self.choose_date_list = tkinter.OptionMenu(self.add_patient_frame, self.choose_date_list_clicked, *self.opp) """
    """     self.choose_date_list.grid(row=0, column=2, padx=20, sticky="news") """
    """"""
    """     self.choose_specializatione_clicked = tkinter.StringVar() """
    """     self.choose_specializatione_clicked.set("choose_specializatione") """
    """     self.choose_specializatione_list = tkinter.OptionMenu(self.add_patient_frame, self.choose_specializatione_clicked, *self.opp) """
    """     self.choose_specializatione_list.grid(row=0, column=3, padx=20, sticky="news") """
    """"""
    """     self.choose_doctor_list_clicked = tkinter.StringVar() """
    """     self.choose_doctor_list_clicked.set("choose doctor") """
    """     self.choose_doctor_list = tkinter.OptionMenu(self.add_patient_frame, self.choose_doctor_list_clicked, *self.opp) """
    """     self.choose_doctor_list.grid(row=0, column=4, padx=20, sticky="news") """
    """"""
    """     for i in range(len(self.buttonNames)): """
    """         tempButton = tkinter.Button(self.tableFrame, text=self.buttonNames[i], font=("Meiryo UI", 18), bg="#1ebbd7", anchor="center") """
    """         tempButton.grid(column=i, row=3, sticky="nsew", padx=15, pady=10) """

    def run(self):
        self.window.mainloop()
