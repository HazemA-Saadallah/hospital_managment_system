import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Login Screen")
root.configure(bg="green")
root.rowconfigure((0), weight=1)
root.columnconfigure((0), weight=1)
root.resizable(False, False)

# intialization of the root
masterFrame = tk.Frame(root)
masterFrame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
masterFrame.columnconfigure((0), weight=1)
# masterFrame.configure(bg="blue")
masterFrame.grid(column=0, row=0, sticky="ew")

# global fonts
messageFont = ("Arial", 18, "bold")
descriptionFont = ("Meiryo UI", 14, "bold")
subdescriptionFont = ("Meiryo UI", 12)
errorFont = ("Meiryo UI", 10)
inputFont = ("Meiryo UI", 12)

# initialization of the company info
companyInfoFrame = tk.Frame(masterFrame)
companyInfoFrame.grid(row=0, column=0, sticky="ew", pady=10)
companyInfoFrame.rowconfigure((0), weight=1)
companyInfoFrame.columnconfigure((0, 1), weight=1)

companyLabelFont = ("Meiryo UI", 24, "bold")
hospitalName = "Al Masreya Hospital"
companyNameLabel = tk.Label(companyInfoFrame, text=hospitalName, font=companyLabelFont, anchor="w")
companyNameLabel.grid(row=0, column=1, sticky="nsew")

companyLogoPath = "./assets/hospitalLogo.png"
companyLogoBitmap = Image.open(companyLogoPath)
""" companyLogoBitmap = companyLogoBitmap.resize((65, 65), Image.ANTIALIAS) """
companyLogoBitmap = companyLogoBitmap.resize((65, 65), Image.Resampling.LANCZOS)
companyLogoImage = ImageTk.PhotoImage(companyLogoBitmap)

companyImageLabel = tk.Label(companyInfoFrame, image=companyLogoImage, anchor="e")
companyImageLabel.grid(column=0, row=0, sticky="nsew")

# login message section
loginMessageFrame = tk.Frame(masterFrame)
loginMessageFrame.grid(row=1, column=0, pady=10, padx=10)
loginMessageFrame.rowconfigure((0, 1), weight=1)
loginMessageFrame.columnconfigure((0), weight=1)

loginMessageLabel = tk.Label(loginMessageFrame, text="Log In:", font=messageFont, anchor="w")
loginMessage = "Please log in with your Employee ID and password"
loginMessageDescriptionLabel = tk.Label(loginMessageFrame, text=loginMessage, font=subdescriptionFont)
loginMessageLabel.grid(column=0, row=1, sticky="w", padx=10)
loginMessageDescriptionLabel.grid(column=0, row=2, sticky="w", padx=10)

# employee id entry section
employeeIDFrame = tk.Frame(masterFrame)
employeeIDFrame.rowconfigure((0, 1, 2), weight=1)
employeeIDFrame.columnconfigure((0), weight=1)
employeeIDFrame.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)
employeeIDLabel = tk.Label(employeeIDFrame, text="Employee ID: ", anchor="w", font=descriptionFont)
employeeIDTextBox = tk.Entry(employeeIDFrame, font=inputFont)
incorrectMessage = "Employee ID does not exist!"
employeIDIncorrectLabel = tk.Label(employeeIDFrame, text=incorrectMessage, anchor="w", fg="red", font=errorFont)
employeeIDLabel.grid(row=0, column=0, sticky="nsew", pady=3, padx=10)
employeeIDTextBox.grid(row=1, column=0, sticky="nsew", padx=10)
employeIDIncorrectLabel.grid(row=2, column=0, sticky="nsew", padx=10)

passwordIDFrame = tk.Frame(masterFrame)
passwordIDFrame.rowconfigure((0, 1, 2), weight=1)
passwordIDFrame.columnconfigure((0), weight=1)
passwordIDFrame.grid(row=3, column=0, sticky="nsew", pady=10, padx=10)
passwordIDLabel = tk.Label(passwordIDFrame, text="Password: ", anchor="w", font=descriptionFont)
passwordIDTextBox = tk.Entry(passwordIDFrame, font=inputFont, show="*")
incorrectMessage = "Password is Incorrect!"
passwordIDIncorrectLabel = tk.Label(passwordIDFrame, text=incorrectMessage, anchor="w", fg="red", font=errorFont)
passwordIDLabel.grid(row=0, column=0, sticky="nsew", pady=3, padx=10)
passwordIDTextBox.grid(row=1, column=0, sticky="nsew", padx=10)
passwordIDIncorrectLabel.grid(row=2, column=0, sticky="w", padx=10)

# remember me check mark
checkBoxFrame = tk.Frame(masterFrame)
checkBoxFrame.rowconfigure((0, 1), weight=1)
checkBoxFrame.columnconfigure((0), weight=1)
checkBoxFrame.grid(row=4, column=0, sticky="nsew", padx=10)
checkBoxVar = tk.BooleanVar()
checkBox = tk.Checkbutton(checkBoxFrame, text="Stay Logged In?", variable=checkBoxVar, font=errorFont)
checkBox.grid(column=0, row=0, sticky="ew")
"""troubleLoginMessage = "Trouble logging in? Contact your system administrator!"
troubleLogin = tk.Label(checkBoxFrame, font=descriptionFont, anchor="center", text=troubleLoginMessage)
troubleLogin.grid(row=1,column=0, sticky="nsew", pady=3)"""

# button section
buttonFrame = tk.Frame(masterFrame)
buttonFrame.rowconfigure((0), weight=1)
buttonFrame.columnconfigure((0), weight=1)
buttonFrame.grid(row=5, column=0, sticky="nsew")
loginButton = tk.Button(buttonFrame, text="Log In", fg="White", bg="Blue", font=descriptionFont, anchor="center")
loginButton.grid(column=0, row=0, pady=10, sticky="nsew", padx=10)

root.mainloop()
