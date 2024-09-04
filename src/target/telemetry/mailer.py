from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Load environment variables from .env file
load_dotenv()

# Email configuration using environment variables
sender_email = os.getenv('SENDER_EMAIL')
password = os.getenv('SENDER_EMAIL_PASSWORD')
receiver_email = os.getenv("RECEIVER_EMAIL")
path_to_encrypted_file = "../target_file_pool/encoded_base64_binary_for_email.bin"

# Set up the server
smtp_server = os.getenv("SMTP_SERVER")
port = os.getenv("PORT")  # For SSL use port 465

#tests
def print_credentials(sender,sender_password,reciever):
    print(f"sender = {sender}\nsender_password = {sender_password}\nreciever = {reciever}")

print_credentials(sender_email,password,receiver_email)
# Create the email content
subject = "Test Email"
body = "Encrypted file"

# Set up the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the body with the msg instance
message.attach(MIMEText(body, "plain"))


# Attach the .bin file
if os.path.isfile(path_to_encrypted_file):
    with open(path_to_encrypted_file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode the payload using Base64
    # encoders.encode_base64(part)
    # Add header for the attachment
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(path_to_encrypted_file)}",
    )

    # Attach the .bin file to the email
    message.attach(part)

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