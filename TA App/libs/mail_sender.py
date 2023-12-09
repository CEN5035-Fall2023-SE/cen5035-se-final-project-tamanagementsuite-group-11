from datetime import datetime
import json
import smtplib

class MailSender:
    def __init__(self, config_file):
        with open(config_file, 'r') as json_file:
            email_config = json.load(json_file)
        
        self.sender_email = email_config.get("sender_email", "")
        self.sender_password = email_config.get("sender_password", "")
        self.recipient_emails = email_config.get("recipient_emails", [])

    def send_application_submission_mail(self):
        if not self.sender_email or not self.sender_password or not self.recipient_emails:
            print("Email configuration is incomplete. Cannot send email.")
            return

        subject = 'Intrusion Alert [Important]'
        message = 'Hey User, System has detected an Intrusion attempt to breach information stored on Azure Database Server. The access has been diverted. Kindly secure the servers.'
        
        for recipient_email in self.recipient_emails:
            self._send_email(recipient_email, subject, message)

    def send_operation_alert_mail(self, operation_name):
        if not self.sender_email or not self.sender_password or not self.recipient_emails:
            print("Email configuration is incomplete. Cannot send email.")
            return

        subject = f'Operation Alert - {operation_name}'
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f'Operation Name: {operation_name}\nTimestamp: {timestamp}'
        
        for recipient_email in self.recipient_emails:
            self._send_email(recipient_email, subject, message)

    def _send_email(self, recipient_email, subject, message):
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(self.sender_email, self.sender_password)
                smtp.sendmail(self.sender_email, recipient_email, f'Subject: {subject}\n\n{message}')
            print(f"Email sent to {recipient_email} with subject: {subject}")
        except Exception as e:
            print(f"Error sending email to {recipient_email}: {str(e)}")

