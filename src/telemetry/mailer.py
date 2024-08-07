from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Load environment variables from .env file
load_dotenv()

# Email configuration using environment variables
sender_email = os.getenv('SENDER_EMAIL')
password = os.getenv('SENDER_EMAIL_PASSWORD')
receiver_email = os.getenv("RECEIVER_EMAIL")

# Set up the server
smtp_server = os.getenv("SMTP_SERVER")
port = os.getenv("PORT")  # For SSL use port 465

#tests
def print_credentials(sender,sender_password,reciever):
    print(f"sender = {sender}\nsender_password = {sender_password}\nreciever = {reciever}")

print_credentials(sender_email,password,receiver_email)
# Create the email content
subject = "Test Email"
body = "This is a test email sent from Python using environment variables."

# Set up the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the body with the msg instance
message.attach(MIMEText(body, "plain"))



try:
    # Start the server
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")

    # Terminate the SMTP session
    server.quit()

except Exception as e:
    print(f"Error: {e}")