import psycopg2
import importlib.util
import sys

main_connection = psycopg2.connect(host="localhost", port="5432", dbname="postgres", user="postgres", password="123")
main_connection_cursor = main_connection.cursor()

spec = importlib.util.spec_from_file_location("GUI", "GUI/GUI.py")
GUI = importlib.util.module_from_spec(spec)
sys.modules["GUI"] = GUI
spec.loader.exec_module(GUI)

spec = importlib.util.spec_from_file_location("login_lookup", "DataBase/login_lookup.py")
login_lookup = importlib.util.module_from_spec(spec)
sys.modules["login_lookup"] = login_lookup
spec.loader.exec_module(login_lookup)


def load_user(user_data: tuple):
    if user_data[5] == 'adminstrator':
        pass


def verify_login_credientials(LGO: GUI.login_screen):
    username = LGO.username_input_box.get()
    password = LGO.passwordIDTextBox.get()
    user_id = login_lookup.lookup_login_name(username)

    if not user_id:
        LGO.flag_login_error('username')
        return
    else:
        LGO.flag_login_error('kill_username')

    if not login_lookup.lookup_password(user_id, password):
        LGO.flag_login_error('password')
        return
    else:
        LGO.flag_login_error('kill_password')

    main_connection_cursor.execute("""SELECT * FROM user_table WHERE user_id = %s""", (user_id,))
    LGO.window.destroy()
    global user_data
    user_data = main_connection_cursor.fetchone()



if __name__ == "__main__":
    login_screen_object = GUI.login_screen()
    login_screen_object.loginButton.configure(command=lambda: verify_login_credientials(login_screen_object))
    login_screen_object.run()
    print(user_data)
    if user_data[4] == 'administrator':
        user_screen = GUI.adminstrator_screen(user_data[3])
        user_screen.run()
    elif user_data[4] == 'reciptionist':
        user_screen = GUI.reciptionist_screen(user_data[3])
        user_screen.run()
    elif user_data[4] == 'doctor':
        user_screen = GUI.doctor_screen(user_data[3])
        user_screen.run()

