import psycopg2
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("hash", "Security/hash.py")
hash = importlib.util.module_from_spec(spec)
sys.modules["hash"] = hash
spec.loader.exec_module(hash)


connection = psycopg2.connect(host="localhost", port="5432", dbname="postgres", user="postgres", password="123")
connection_cursor = connection.cursor()


def lookup_login_name(login_name: str) -> bool:
    connection_cursor.execute("""SELECT user_id FROM login_name_linker_table WHERE login_name = %s""", (login_name,))
    return connection_cursor.fetchone()


def lookup_password(user_id: str, password: str):
    connection_cursor.execute("""SELECT password_salt, password_hash FROM user_table WHERE user_id = %s""", (user_id,))
    fetched_data = connection_cursor.fetchone()
    return fetched_data[1] == hash.hash(password, fetched_data[0])


""" def run(login_name: str, password: str): """
"""     id = lookup_login_name(login_name) """
"""     if id: """
"""         verification = lookup_password(id, password) """
"""         if verification: return True """
"""         else: return """



if __name__ == "__main__":
    print("lookup user200: ", lookup_login_name("user200"))
    admin_id = lookup_login_name("admin")[0]
    print("lookup admin: ", admin_id)
    print("lookup admin with 123: ", lookup_password(admin_id, '123'))
    print("lookup admin with admin: ", lookup_password(admin_id, 'admin'))
    print("lookup admin with None value: ", lookup_password(admin_id, str(None)))
