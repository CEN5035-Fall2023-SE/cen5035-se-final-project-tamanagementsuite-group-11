import pyodbc
import json

class DatabaseManager:
    def __init__(self, config_file):
        with open(config_file, 'r') as json_file:
            config = json.load(json_file)
        
        self.conn_str = (
            f"Driver={config['Driver']};"
            f"Server=tcp:{config['ServerName']},1433;"
            f"Database={config['DatabaseName']};"
            f"Uid={config['UserID']};"
            f"Pwd={config['Password']};"
            f"Encrypt={config['Encrypt']};"
            f"TrustServerCertificate={config['TrustServerCertificate']};"
            f"Connection Timeout={config['ConnectionTimeout']};"
        )

    def get_conn_obj(self):
        conn_string = self.conn_str
        conn = pyodbc.connect(conn_string)
        return conn
    
db = DatabaseManager('config/db_config.json')
print(db.get_conn_obj())



#-------------------TA Applicant------------------------

import pyodbc
import json
from datetime import datetime

class DatabaseManager:
    def __init__(self, config_file):
        with open(config_file, 'r') as json_file:
            config = json.load(json_file)
        
        self.conn_str = (
            f"Driver={config['Driver']};"
            f"Server=tcp:{config['ServerName']},1433;"
            f"Database={config['DatabaseName']};"
            f"Uid={config['UserID']};"
            f"Pwd={config['Password']};"
            f"Encrypt={config['Encrypt']};"
            f"TrustServerCertificate={config['TrustServerCertificate']};"
            f"Connection Timeout={config['ConnectionTimeout']};"
        )

    def get_conn_obj(self):
        return pyodbc.connect(self.conn_str)

def ta_applicant_register_user(db_manager):
    username = input("Enter username: ")
    password = input("Enter password: ")  # Hash this password in production
    email = input("Enter email: ")
    role = "TA"  # Assuming the role is always TA for this script

    conn = db_manager.get_conn_obj()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Users (Username, Password, Email, Role) VALUES (?, ?, ?, ?)", 
                   (username, password, email, role))
    user_id = cursor.execute("SELECT @@IDENTITY AS ID;").fetchval()
    print(f'Your user_id is {user_id}')
    print('Details needed to create user profile:')
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    contact_number = input("Enter contact number: ")
    address = input("Enter address: ")
    additional_info = input("Enter additional information: ")

    cursor.execute("INSERT INTO UserProfile (UserID, FirstName, LastName, ContactNumber, Address, AdditionalInformation) VALUES (?, ?, ?, ?, ?, ?)", 
                   (user_id, first_name, last_name, contact_number, address, additional_info))
    
    conn.commit()
    conn.close()

    print("Registration successful.")

def ta_applicant_submit_application(db_manager):
    user_id = input("Enter your User ID: ")
    course_id = input("Enter the Course ID you are applying for: ")
    cv_link = input("Enter the link to your CV: ")
    status = "Received"
    submission_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = db_manager.get_conn_obj()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Applications (UserID, CourseID, CV, Status, SubmissionDate) VALUES (?, ?, ?, ?, ?)", 
                   (user_id, course_id, cv_link, status, submission_date))

    conn.commit()
    conn.close()

    print("Application submitted successfully.")

def ta_applicant_menu():
    print('Selected TA Applicant')
    db_manager = DatabaseManager('config/db_config.json')
    while True:
        print("TA Management System")
        print("1. Register as a TA")
        print("2. Submit TA Application")
        choice = input("Enter your choice: ")

        if choice == '1':
            ta_applicant_register_user(db_manager)
        elif choice == '2':
            ta_applicant_submit_application(db_manager)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    print('Select user type:\n')
    print('1) TA Applicant')
    print('2) TA Management')
    print('3) TA Staff')
    print('4) Instructors')

    choice = input("Enter your choice: ")
    if choice == '1':
        ta_applicant_menu()
    main()

