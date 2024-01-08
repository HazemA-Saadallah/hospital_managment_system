from tkinter import ttk
from commonFunctions import tk, loadImage


root = tk.Tk()
root.title("Admin Screen")
root.wm_state("normal")
root.columnconfigure((0), weight=1)
root.rowconfigure((0), weight=1)
masterFrame = tk.Frame(root)
masterFrame.rowconfigure((0), weight=1)
masterFrame.columnconfigure((0), weight=1)
masterFrame.grid(column=0, row=0, sticky="nsew")

# global variables
welcomeFont = ("Meiryo UI", 40, "bold")
submessageFont = ("Meiryo UI", 18)
submessageFontFin = ("Meiryo UI", 24, "bold")
logoutFont = ("Meiryo UI", 12, "bold")
patientFont = ("Meiryo UI", 36, "bold")
tableFontHeading = ("Lucidia Sans", 17, "bold")
tableFont = ("Lucidia Sans", 12)
profilePictureImage = loadImage("./assets/noPersonBorderless.png", 280, 280)
""" profilePictureImage = loadImage("./assets/noPersonBorderless.png", 100, 100) """

# State Variables
HOME_STATE = False
HOME_VAR = []

HOSPITAL_VAR = []
HOSPITAL_STATE = False

FINANCIAL_VAR = []
FINANCIAL_STATE = False

# functions


# HOME SECTION
def createHome():
    global HOME_STATE
    global HOME_VAR
    if not HOME_STATE:
        welcomeFrame = tk.Frame(master=masterFrame)
        welcomeFrame.rowconfigure((0, 1, 2), weight=1)
        welcomeFrame.columnconfigure((0), weight=1)
        welcomeFrame.grid(row=0, column=0, sticky="nsew")

        pictureLabel = tk.Label(master=welcomeFrame, image=profilePictureImage, anchor="s")
        welcomeMessage = "Welcome Mahmoud Hussein Elsaadawy!"
        subWelcomeMessage = "Please select a mode to continue from the system menu"
        textLabel = tk.Label(master=welcomeFrame, text=welcomeMessage, anchor="n", font=welcomeFont)
        subTextLabel = tk.Label(master=welcomeFrame, text=subWelcomeMessage, anchor="n", font=submessageFont)
        pictureLabel.grid(row=0, column=0, padx=10, sticky="s")
        textLabel.grid(row=1, column=0, padx=10, sticky="ew")
        subTextLabel.grid(row=2, column=0, padx=10, sticky="n")
        HOME_VAR.append(welcomeFrame)
        HOME_STATE = True


def destroyHome():
    global HOME_VAR
    global HOME_STATE
    if HOME_STATE:
        for obj in HOME_VAR:
            obj.destroy()
        HOME_STATE = False


# HOSPITAL SECTION
def createHospitalSection():
    global HOSPITAL_VAR
    global HOSPITAL_STATE
    if not HOSPITAL_STATE:
        hospitalFrame = tk.Frame(master=root)
        hospitalFrame.columnconfigure((0), weight=1)
        hospitalFrame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18), weight=1)
        hospitalFrame.grid(row=0, column=0, sticky="nsew")

        # welcome message
        hospitalManagementMessage = tk.Label(master=hospitalFrame, text="Hospital Management:", anchor="w")
        hospitalManagementMessage.grid(row=0, column=0, sticky="ew")

        # Specialization config
        specializationLabel = tk.Label(master=hospitalFrame, text="Specializations:", anchor="w")
        specializationEntry = tk.Entry(master=hospitalFrame)
        specializationMessage = "Please seperate each specialization with a '-'"
        specializationTip = tk.Label(master=hospitalFrame, text=specializationMessage, anchor="w")
        specializationLabel.grid(row=1, column=0, sticky="ew")
        specializationEntry.grid(row=2, column=0, sticky="ew")
        specializationTip.grid(row=3, column=0, sticky="ew")

        # Priority management config
        priorityLabel = tk.Label(master=hospitalFrame, text="Priorities: ", anchor="w")
        priorityEntry = tk.Entry(master=hospitalFrame)
        priorityMessage = "Write a Priority name seperated with a '_' and ends with a number. 'Very_Urgent3' is an example"
        priorityTip = tk.Label(master=hospitalFrame, text=priorityMessage, anchor="w")
        priorityLabel.grid(row=4, column=0, sticky="ew")
        priorityEntry.grid(row=5, column=0, sticky="ew")
        priorityTip.grid(row=6, column=0, sticky="ew")

        # doctor management config
        doctorLabel = tk.Label(master=hospitalFrame, text="Doctor Schedule Configuration:", anchor="w")
        table = ttk.Treeview(hospitalFrame, columns=('id', 'name', 'date', 'record'), show="headings")
        table.heading(('id'), text="Patient ID")
        table.heading(('name'), text="Full Name")
        table.heading(('date'), text="Appointment Time")
        table.heading(('record'), text="Medical Record")
        verticalScrollBar = ttk.Scrollbar(root, orient="vertical", command=table.yview)
        table.configure(yscrollcommand=verticalScrollBar.set)
        doctorLabel.grid(row=7, column=0, sticky="ew")
        table.grid(row=8, rowspan=4, column=0, sticky="ew")

        # Table Buttons section
        buttonNames = ["Remove Patient", "Delete Patient", "Edit Patient", "Transfer Patient", "View Medical Record", "View Full Information"]
        buttonFrame = tk.Frame(master=hospitalFrame)
        buttonFrame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        buttonFrame.grid(row=13, column=0, sticky="ew")
        for i in range(len(buttonNames)):
            tempButton = tk.Button(buttonFrame, text=buttonNames[i], font=submessageFont, bg="#1ebbd7", anchor="center")
            tempButton.grid(column=i, row=0, sticky="nsew", padx=15, pady=10)

        # now at row 14 and users table
        # registered users section
        registeredUsersLabel = tk.Label(master=hospitalFrame, text="Registered System Users: ", anchor="w")
        usersTable = ttk.Treeview(hospitalFrame, columns=("name", "empid", "type", "specialization"), show="headings")
        usersTable.heading(('name'), text="User Name")
        usersTable.heading(('empid'), text="User ID")
        usersTable.heading(('type'), text="User Type")
        usersTable.heading(('specialization'), text="Specialization")
        verticalScrollBar = ttk.Scrollbar(root, orient="vertical", command=usersTable.yview)
        usersTable.configure(yscrollcommand=verticalScrollBar.set)
        registeredUsersLabel.grid(row=14, column=0, sticky="ew")
        usersTable.grid(row=15, rowspan=2, column=0, sticky="ew")

        # now at row 18
        userButtons = ["Delete User", "Add User", "Edit User", "View User Data"]
        userButtonFrame = tk.Frame(master=hospitalFrame)
        userButtonFrame.rowconfigure((0), weight=1)
        userButtonFrame.columnconfigure((0, 1, 2, 3), weight=1)
        userButtonFrame.grid(row=18, column=0, sticky="ew")
        for i in range(len(userButtons)):
            tempUserButton = tk.Button(master=userButtonFrame, text=userButtons[i], bg="#1ebbd7", font=submessageFont, anchor="center")
            tempUserButton.grid(row=0, column=i, sticky="nsew", padx=15)
        HOSPITAL_VAR.append(hospitalFrame)
        HOSPITAL_STATE = True

def destroyHospital():
    global HOSPITAL_STATE
    global HOSPITAL_VAR
    if HOSPITAL_STATE:
        for obj in HOSPITAL_VAR:
            obj.destroy()
        HOSPITAL_STATE = False


def createFinancial():
    global FINANCIAL_STATE
    global FINANCIAL_VAR
    if not FINANCIAL_STATE:
        financialFrame = tk.Frame(master=masterFrame)
        financialFrame.rowconfigure((0, 1, 2, 3, 4), weight=1)
        financialFrame.columnconfigure((0), weight=1)
        financialFrame.grid(column=0, row=0, sticky="nsew")
        finTitleLabel = tk.Label(master=financialFrame, text="Financial Management", anchor="center", font=patientFont)
        finTitleLabel.grid(row=0, column=0, sticky="ew")
        finTable = ttk.Treeview(financialFrame, show="headings", columns=("transName", "transID", "cashIn", "cashOut"))
        finTable.heading(("transName"), text="Transaction Name")
        finTable.heading(("transID"), text="Transaction ID")
        finTable.heading(("cashIn"), text="Cash In")
        finTable.heading(("cashOut"), text="Cash Out")
        finTable.grid(row=1, rowspan=3, column=0, sticky="nsew")

        cashFlows = ["Revenue: XXXX", "Expenses: YYYY", "Profit: ZZZZ"]
        cashFlowsFrame = tk.Frame(financialFrame)
        cashFlowsFrame.rowconfigure((0), weight=1)
        cashFlowsFrame.columnconfigure((0, 1, 2), weight=1)
        cashFlowsFrame.grid(row=4, column=0, sticky="nsew")
        for i in range(len(cashFlows)):
            cashFlowButton = tk.Label(master=cashFlowsFrame, text=cashFlows[i], anchor="center", font=submessageFontFin)
            cashFlowButton.grid(column=i, row=0, sticky="ew", padx=15)

        FINANCIAL_STATE = True
        FINANCIAL_VAR.append(financialFrame)


def destroyFinancial():
    global FINANCIAL_VAR
    global FINANCIAL_STATE
    if FINANCIAL_STATE:
        for obj in FINANCIAL_VAR:
            obj.destroy()
        FINANCIAL_STATE = False


def goToHospital():
    destroyHome()
    destroyFinancial()
    createHospitalSection()


def goToFinancial():
    destroyHome()
    destroyHospital()
    createFinancial()


def goToHome():
    # Destroy the rest of the things
    destroyHospital()
    destroyFinancial()
    createHome()


# to Change
createHome()

# Menu initialization
masterMenu = tk.Menu(root)
root.config(menu=masterMenu)
modeMenu = tk.Menu(master=masterMenu)
masterMenu.add_cascade(label="Mode", menu=modeMenu)
modeMenu.add_command(label="Home", command=goToHome)
modeMenu.add_separator()
modeMenu.add_command(label="Financial Management", command=goToFinancial)
modeMenu.add_separator()
modeMenu.add_command(label="Hospital Management", command=goToHospital)

root.mainloop()
