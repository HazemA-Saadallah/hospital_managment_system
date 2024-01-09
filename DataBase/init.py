import psycopg2
import importlib.util
import sys
import random

spec = importlib.util.spec_from_file_location("hash", "Security/hash.py")
hash = importlib.util.module_from_spec(spec)
sys.modules["hash"] = hash
spec.loader.exec_module(hash)


class DB_builder:
    def __init__(self) -> None:
        self.connection = psycopg2.connect(host="localhost", port="5432", dbname="postgres", user="postgres", password="123")
        self.connection_cursor = self.connection.cursor()
        self.drop_all_tables()
        self.create_user_db()
        self.create_login_name_linker_db()
        self.create_medical_record_db()
        self.create_reports_database()
        self.create_appointment_database()
        self.connection_cursor.execute("""ALTER SEQUENCE user_table_user_id_seq RESTART WITH 320220001;""")
        self.connection_cursor.execute("""ALTER SEQUENCE login_name_linker_table_user_id_seq RESTART WITH 320220001;""")
        """ self.connection_cursor.close() """
        """ self.connection.close() """

    def create_user_db(self):
        self.connection_cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_table (
                user_id SERIAL PRIMARY KEY,
                password_salt VARCHAR(32),
                password_hash VARCHAR(256),
                user_name VARCHAR,
                user_type VARCHAR,
                specialization VARCHAR,
                user_image BYTEA
            );
        """)
        self.connection.commit()

    def create_login_name_linker_db(self):
        self.connection_cursor.execute("""
            CREATE TABLE IF NOT EXISTS login_name_linker_table (
                login_name VARCHAR PRIMARY KEY,
                user_id SERIAL
            );
        """)
        self.connection.commit()

    def create_medical_record_db(self):
        self.connection_cursor.execute("""
            CREATE TABLE IF NOT EXISTS medical_records (
                record_id INT PRIMARY KEY,
                patient_id VARCHAR,
                patient_age INT,
                doctor_id INT,
                record_date_time TIMESTAMP
            );
        """)
        self.connection.commit()

    def create_reports_database(self):
        self.connection_cursor.execute("""
            CREATE TABLE IF NOT EXISTS patient_report (
                record_id INT PRIMARY KEY,
                report BYTEA
            );
        """)
        self.connection.commit()

    def create_appointment_database(self):
        self.connection_cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointment_database (
                appointment_id INT PRIMARY KEY,
                patient_id INT,
                patient_name VARCHAR,
                appointment_date DATE,
                appointment_time TIME,
                doctor_id INT
            )
        """)
        self.connection.commit()

    def drop_all_tables(self):
        self.connection_cursor.execute("""
            DROP SCHEMA public CASCADE;
            CREATE SCHEMA public;
            GRANT ALL ON SCHEMA public TO postgres;
            GRANT ALL ON SCHEMA public TO public;
        """)
        self.connection.commit()

    # def truncate_all_tables(self):
    #     self.connection_cursor.execute("""SELECT 'TRUNCATE TABLE ' ||  tablename || ';' FROM pg_tables;""")
    #     self.connection.commit()

    def generate_dummy_users(self, number_of_users: int) -> None:
        user_types = ["doctor", "reciptionist", "administrator"]
        specialization_list = ["Allergy and immunology", "Anesthesiology", "Dermatology", "Diagnostic radiology", "Emergency medicine", "Family medicine", "Internal medicine" 
                               "Medical genetics", "Neurology", "Nuclear medicine", "Obstetrics and gynecology", "Ophthalmology", "Pathology", "Pediatrics",
                               "Physical medicine and rehabilitation", "Preventive medicine", "Psychiatry", "Radiation oncology", "Surgery", "Urology"]
        password_couple = hash.genrate_hash_and_salt("admin")
        self.connection_cursor.execute('''INSERT INTO user_table (password_salt, password_hash, user_name, user_type) VALUES (%s, %s, %s, %s)''',
                                       (password_couple[0], password_couple[1], "manager", "administrator"))
        self.connection_cursor.execute("""INSERT INTO login_name_linker_table (login_name) VALUES ('admin')""")

        for i in range(number_of_users - 1):
            password_couple = hash.genrate_hash_and_salt("abc")
            random_choice = user_types[random.randint(0, 2)]
            if random_choice == 'administrator' or random_choice == 'reciptionist':
                self.connection_cursor.execute('''INSERT INTO user_table (password_salt, password_hash, user_name, user_type) VALUES (%s, %s, %s, %s)''',
                                              (password_couple[0], password_couple[1], f"mr.user{i}", random_choice))
            else:
                self.connection_cursor.execute('''INSERT INTO user_table (password_salt, password_hash, user_name, user_type, specialization) VALUES (%s, %s, %s, %s, %s)''',
                                              (password_couple[0], password_couple[1], f"mr.user{i}", random_choice, specialization_list[random.randint(0, 18)]))

            self.connection_cursor.execute("""INSERT INTO login_name_linker_table (login_name) VALUES (%s)""", (f"user{i}",))
            self.connection.commit()


if __name__ == "__main__":
    init = DB_builder()
    """ init.drop_all_tables() """
    init.generate_dummy_users(100)
    """ init.truncate_all_tables() """
