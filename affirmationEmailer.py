import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

def get_random_affirmation():
    # Add a list of affirmations here
    affirmations = [
        "You are capable of amazing things.",
        "Your potential is limitless.",
        "You are deserving of love and happiness.",
        # Add more affirmations as needed
    ]
    return random.choice(affirmations)

def send_email(to_email, subject, body):
    # Email configuration (update with your SMTP server details)
    smtp_server = 'your_smtp_server.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    # Email setup
    sender_email = 'your_email@example.com'
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Establish a connection with the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Start TLS for security
        server.starttls()

        # Login to the email account
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())

if __name__ == "__main__":
    # Replace 'recipient@example.com' with the actual recipient's email address
    recipient_email = 'recipient@example.com'
    
    # Customize the subject and body of the email
    email_subject = 'Daily Affirmation'
    affirmation_body = get_random_affirmation()

    # Send the email
    send_email(recipient_email, email_subject, affirmation_body)