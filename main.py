import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time


def send_email():
    # Replace the following variables with your data
    sender_email = "your_address@gmail.com"
    sender_password = "your_password"
    recipient_email = "recipient@gmail.com"

    subject = "Daily Report"
    body = "Text of your daily report."

    # Setting up the letter
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to Gmail server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())


# Set up a schedule to send daily reports at 12:00 every day
schedule.every().day.at("12:00").do(send_email)

# Infinite loop to execute the schedule
while True:
    schedule.run_pending()
    time.sleep(1)
