import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
import random

class login_screen:
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Login")
        self.window.resizable(False, False)
        self.masterframe = tkinter.Frame(self.window)
        self.masterframe.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.masterframe.columnconfigure((0), weight=1)
        self.masterframe.grid(column=0, row=0, sticky="ew")
        self.logo = Image.open("./assets/hospitalLogo.png")

    def init_logo(self):
        logo_frame = tkinter.Frame(self.masterframe)
        logo_frame.grid(row=0, column=0, sticky="ew", pady=10)
        logo_frame.rowconfigure((0), weight=1)
        logo_frame.columnconfigure((0, 1), weight=1)

        logo_label = tkinter.Label(logo_frame, text="F-JUST", font=("Meiryo UI", 24, "bold"), anchor="w")
        logo_label.grid(row=0, column=1, sticky="nsew")

        self.logo = self.logo.resize((65, 65), Image.Resampling.LANCZOS)
        self.companyLogoImage = ImageTk.PhotoImage(self.logo)
        companyImageLabel = tkinter.Label(logo_frame, image=self.companyLogoImage, anchor="e")
        companyImageLabel.grid(column=0, row=0, sticky="nsew")

    def init_login_massage(self):
        massage_frame = tkinter.Frame(self.masterframe)
        massage_frame.grid(row=1, column=0, pady=10, padx=10)
        massage_frame.rowconfigure((0, 1), weight=1)
        massage_frame.columnconfigure((0), weight=1)
        loginMessageLabel = tkinter.Label(massage_frame, text="Log In:", font=("Arial", 18, "bold"), anchor="w")
        loginMessageDescriptionLabel = tkinter.Label(massage_frame, text="Please log in with your Employee ID and password", font=("Meiryo UI", 12))
        loginMessageLabel.grid(column=0, row=1, sticky="w", padx=10)
        loginMessageDescriptionLabel.grid(column=0, row=2, sticky="w", padx=10)

    def init_username_section(self):
        username_input_frame = tkinter.Frame(self.masterframe)
        username_input_frame.rowconfigure((0, 1, 2), weight=1)
        username_input_frame.columnconfigure((0), weight=1)
        username_input_frame.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)
        username_input_label = tkinter.Label(username_input_frame, text="Employee ID: ", anchor="w", font=("Meiryo UI", 14, "bold"))
        username_input_box = tkinter.Entry(username_input_frame, font=("Meiryo UI", 12))
        username_input_label.grid(row=0, column=0, sticky="nsew", pady=3, padx=10)
        username_input_box.grid(row=1, column=0, sticky="nsew", padx=10)

        wrong_username_label = tkinter.Label(username_input_frame, text="Employee ID does not exist!", anchor="w", fg="red", font=("Meiryo UI", 10))
        return wrong_username_label

    def init_password_section(self):
        passwordIDFrame = tkinter.Frame(self.masterframe)
        passwordIDFrame.rowconfigure((0, 1, 2), weight=1)
        passwordIDFrame.columnconfigure((0), weight=1)
        passwordIDFrame.grid(row=3, column=0, sticky="nsew", pady=10, padx=10)
        passwordIDLabel = tkinter.Label(passwordIDFrame, text="Password: ", anchor="w", font=("Meiryo UI", 14, "bold"))
        passwordIDTextBox = tkinter.Entry(passwordIDFrame, font=("Meiryo UI", 12), show="*")
        passwordIDLabel.grid(row=0, column=0, sticky="nsew", pady=3, padx=10)
        passwordIDTextBox.grid(row=1, column=0, sticky="nsew", padx=10)

        wrong_password_label = tkinter.Label(passwordIDFrame, text="password is incorrect!", anchor="w", fg="red", font=("Meiryo UI", 10))
        return wrong_password_label

    def init_button_section(self):
        buttonFrame = tkinter.Frame(self.masterframe)
        buttonFrame.rowconfigure((0), weight=1)
        buttonFrame.columnconfigure((0), weight=1)
        buttonFrame.grid(row=5, column=0, sticky="nsew")
        loginButton = tkinter.Button(buttonFrame, text="Log In", fg="White", bg="Blue", font=("Meiryo UI", 14, "bold"), anchor="center")
        loginButton.grid(column=0, row=0, pady=10, sticky="nsew", padx=10)

    def flag_login_error(self, error_code):
        wrong_username_label = self.init_username_section()
        wrong_password_label = self.init_password_section()

        if error_code == 'username':
            wrong_username_label.grid(row=2, column=0, sticky="nsew", padx=10)
        elif error_code == 'password':
            wrong_password_label.grid(row=2, column=0, sticky="w", padx=10)
        elif error_code == 'both':
            wrong_username_label.grid(row=2, column=0, sticky="nsew", padx=10)
            wrong_password_label.grid(row=2, column=0, sticky="w", padx=10)

    def run(self):
        self.init_logo()
        self.init_login_massage()
        self.init_username_section()
        self.init_password_section()
        self.init_button_section()
        self.window.mainloop()


class adminstrator_screen:
    def __init__(self) -> None:
        pass

    def run(self):
        pass


class reciptionist_screen:
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Receptionist Screen")
        self.window.wm_state("normal")
        self.window.columnconfigure((0), weight=1)
        self.window.rowconfigure((0), weight=1)
        self.masterframe = tkinter.Frame(self.window)
        self.masterframe.rowconfigure((0, 1, 2), weight=1)
        self.masterframe.columnconfigure((0), weight=1)
        self.masterframe.grid(column=0, row=0, sticky="nsew")
        self.profilePictureImage = Image.open("./assets/noPersonBorderless.png")
        self.logoutImage = Image.open("./assets/logout.png")

    def init_user_data_section(self):
        self.profilePictureImage = self.profilePictureImage.resize((180, 180), Image.Resampling.LANCZOS)
        self.profilePictureImage = ImageTk.PhotoImage(self.profilePictureImage)
        user_data_section = tkinter.Frame(self.masterframe)
        user_data_section.grid(column=0, row=0, sticky="nsew")
        user_data_section.columnconfigure((0, 1, 2), weight=1)
        user_data_section.rowconfigure((0, 1), weight=1)
        welcomeMessage = "Welcome Sara Mohamed Elbassiouny!"
        patientsMessage = "There are currently XYZ appointments"
        welcomeLabel = tkinter.Label(user_data_section, text=welcomeMessage, font=("Meiryo UI", 36, "bold"), anchor="sw")
        patientsLabel = tkinter.Label(user_data_section, text=patientsMessage, font=("Meiryo UI", 18), anchor="nw")
        pictureLabel = tkinter.Label(user_data_section, image=self.profilePictureImage)
        welcomeLabel.grid(column=1, row=0, padx=20,  sticky="nsw")
        patientsLabel.grid(column=1, row=1, padx=20, sticky="nsew")
        pictureLabel.grid(column=0, row=0, rowspan=2, padx=20, sticky="nsew")

        self.logoutImage = self.logoutImage.resize((50, 50), Image.Resampling.LANCZOS)
        self.logoutImage = ImageTk.PhotoImage(self.logoutImage)
        logoutFrame = tkinter.Frame(user_data_section)
        logoutFrame.rowconfigure((0, 1), weight=1)
        logoutFrame.columnconfigure((0), weight=1)
        logoutFrame.grid(column=2, row=0, sticky="ew", columnspan=1)
        logoutImageButton = tkinter.Button(logoutFrame, image=self.logoutImage, anchor="e")
        logoutImageButton.grid(row=0, column=0, padx=20, pady=2, sticky="ne")
        logoutText = tkinter.Label(logoutFrame, text="Log out?", font=("Meiryo UI", 12, "bold"), anchor="e")
        logoutText.grid(column=0, row=1, padx=10, sticky="e")

    def init_table(self):
        tableFrame = tkinter.Frame(self.masterframe)
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

    def run(self):
        self.init_user_data_section()
        self.init_table()
        self.window.mainloop()


class doctor_screen:
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Doctor Screen")
        self.window.wm_state("normal")
        self.window.columnconfigure((0), weight=1)
        self.window.rowconfigure((0), weight=1)
        self.masterframe = tkinter.Frame(self.window)
        self.masterframe.rowconfigure((0, 1, 2), weight=1)
        self.masterframe.columnconfigure((0), weight=1)
        self.masterframe.grid(column=0, row=0, sticky="nsew")
        self.profilePictureImage = Image.open("./assets/noPersonBorderless.png")
        self.logoutImage = Image.open("./assets/logout.png")

    def init_user_data_section(self):
        self.profilePictureImage = self.profilePictureImage.resize((180, 180), Image.Resampling.LANCZOS)
        self.profilePictureImage = ImageTk.PhotoImage(self.profilePictureImage)
        user_data_frame = tkinter.Frame(self.masterframe)
        user_data_frame.grid(column=0, row=0, sticky="nsew")
        user_data_frame.columnconfigure((0, 1, 2), weight=1)
        user_data_frame.rowconfigure((0, 1), weight=1)
        welcomeMessage = "Welcome Dr. Bassem Mohamed Elsaadany!"
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
        ttkStyle.configure("Treeview", font=("Lucidia Sans", 12), rowheight=50)
        ttkStyle.configure("Treeview.Heading", font=("Lucidia Sans", 17, "bold"))
        self.table = ttk.Treeview(self.tableFrame, columns=('id', 'name', 'date', 'record'), show="headings", height=30)
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
        sources = ["Hospital", "Reception", "Transfer", "Hospital Transfer"]
        firstNames = ["John", "Tom", "Jones", "Mohamed", "Cliff", "Arriana", "Melissa"]
        lastNames = ["Thomas", "Sombol", "Hambola", "Mohsen", "Alshishi", "AlFerdesy", "Dynamite"]
        date = "XX/YY/ZZ"
        for i in range(30):
            firstName = random.choice(firstNames)
            lastName = random.choice(lastNames)
            reason = random.choice(sources)
            fullName = firstName + " " + lastName
            record = firstName.lower() + "_" + lastName.lower() + ".xlsx"
            data = (i, fullName, "XX/YY/ZZ XX:YY PM", record)
            self.table.insert(parent="", index=tkinter.END, values=data)

    def run(self):
        self.init_user_data_section()
        self.init_table()
        self.table_inser_dumy_data()
        self.window.mainloop()
        pass


if __name__ == "__main__":
    """ login = login_screen() """
    """ login.run() """

    """ reciptionist = reciptionist_screen() """
    """ reciptionist.run() """

    doctor = doctor_screen()
    doctor.run()
