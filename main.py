import importlib.util
import sys


spec = importlib.util.spec_from_file_location("GUI", "GUI/GUI.py")
GUI = importlib.util.module_from_spec(spec)
sys.modules["GUI"] = GUI
spec.loader.exec_module(GUI)


@staticmethod
def cridentioals_getter(obj: GUI.login_screen):
    username = obj.username_input_box.get()
    password = obj.passwordIDTextBox.get()


def lunch_login_screen():
    login_screen_obj = GUI.login_screen()
    login_screen_obj.run()
    login_screen_obj.loginButton.configure(text="aa")


if __name__ == "__main__":
    lunch_login_screen()
