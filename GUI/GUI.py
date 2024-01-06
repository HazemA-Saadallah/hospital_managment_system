import tkinter
from PIL import Image, ImageTk


def load_image(location):
    img = Image.open(location)
    return img


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


class doctor_screen:
    def __init__(self) -> None:
        pass

    def run(self):
        pass

if __name__ == "__main__":
    login = login_screen()
    login.run()
