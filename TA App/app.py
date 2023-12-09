import pypyodbc
from flask import Flask, render_template, redirect, request
from pathlib import Path
import smtplib
import json
import time
import os
from libs.mail_sender import *

class DatabaseManager:
    def __init__(self, config_file):
        with open(config_file, 'r') as json_file:
            config = json.load(json_file)
        
        self.driver = (
            f"Driver={config['Driver']};"
            f"Server=tcp:{config['ServerName']},1433;"
            f"Database={config['DatabaseName']};"
            f"Uid={config['UserID']};"
            f"Pwd={config['Password']};"
            f"Encrypt={config['Encrypt']};"
            f"TrustServerCertificate={config['TrustServerCertificate']};"
            f"Connection Timeout={config['ConnectionTimeout']};"
        )


class TAManagementSuite:
    def __init__(self):
        self.app = Flask(__name__)

        self.my_str = ""
        
        #self.db_manager = DatabaseManager('config/db_config.json')
        #self.email_sender = MailSender('config/email_config.json')
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/TAManagementSuite')
        def entry_page():
            self.fail_count = 0
            self.genuine_DBA = True
            return render_template("userselection_index.html")

        @self.app.route('/TAManagementSuite/ta_applicant_login')
        def ta_applicant_login():
            print('ta_applicant_login')
            return render_template("appform_index.html")


    def run(self):
        print("To access application, go to:","http://127.0.0.1:7000/TAManagementSuite\n\n\nServer Traffic and other details:\n")
        self.app.run(host="127.0.0.1", port=7000)

if __name__ == '__main__':
    ta_management_suite = TAManagementSuite()
    ta_management_suite.run()
