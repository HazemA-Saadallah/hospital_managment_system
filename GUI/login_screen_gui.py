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
