from email import message
from email.quoprimime import body_check
import smtplib
import ssl
from email.message import EmailMessage
import imghdr

subject = "Welcome to our Newsletter"
sender_email = "chiamakambah22@gmail.com"
receiver_emails = ["annakene18@gmail.com", "annakene17@gmail.com"]
password = input("Enter password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = ",".join(receiver_emails)
message["Subject"] = subject

#to attach html file to send as email
with open('index.html', 'r') as f:
   html_string = f.read()

html = html_string
message.add_alternative(html, subtype="html")

#to attach image to send as email
with open('Automate Email.png', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name
message.add_attachment(image_data, maintype='image',
                          subtype=image_type, filename=image_name)

#to attach pdf file to send as email
with open("Newsletter.pdf", 'rb') as f:
        file_data = f.read()
        file_name = f.name
message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

context = ssl.create_default_context()

print("Sending Email")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_emails, message.as_string())

print("Email Sent!")   
