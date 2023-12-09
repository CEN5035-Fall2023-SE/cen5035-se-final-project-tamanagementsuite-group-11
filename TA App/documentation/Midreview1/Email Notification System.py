from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Mock SendGrid API Key for illustrative purposes. In a real-world scenario, this should be a valid key.
SENDGRID_API_KEY = 'SG.mock_1234567890abcdefghijklmnop'

def send_email(recipient_email, subject, content):
    """Send email using SendGrid."""
    message = Mail(
        from_email='noreply@northuniversityta.edu',
        to_emails=recipient_email,
        subject=subject,
        plain_text_content=content
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
    except Exception as e:
        print(e)

# Example usage:
send_email('student@northuniversityta.edu', 'TA Assignment', 'You have been assigned to CS101.')
