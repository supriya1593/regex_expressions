import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
x = True
while x:
  pattern = re.compile(r'^[A-Za-z ]+')
  text = input("Enter Name: ")
  matches = pattern.fullmatch(text)
  if matches != None:
    name = matches.group()
    x = False
  else:
    print("Enter Name in correct format")
print(name)
x = True
while x:
  pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
  dob1 = input("Enter Date of Birth: ")
  matches = pattern.fullmatch(dob1)
  if matches != None:
    dob = matches.group()
    x = False
  else:
    print("Enter DOB in correct format")
print(dob)
x = True
while x:
  pattern = re.compile(r'^[6789]\d{2}-\d{3}-\d{4}')
  phone1 = input("Enter Mobile Number: ")
  matches = pattern.fullmatch(phone1)
  if matches != None:
    phone = matches.group()
    x = False
  else:
    print("Enter Mobile in correct format")
print(phone)
insta = input("Enter Insta Id: ")
print(insta)
while True:
    pattern = re.compile(r'^[a-zA-Z0-9]+@gmail\.com$')
    email1 = input("Enter Email: ")
    if pattern.fullmatch(email1):
        email = email1
        break
    else:
        print("Enter Email in correct format (example@gmail.com)")

print(email)
#sending Mail
SENDER_EMAIL = "vamsipriyalakku6@gmail.com" 
SENDER_PASSWORD = "dvww hgij zxlh wfkn" 

RECEIVER_EMAIL = email  
subject = "Your Entered Details"
body = f"""
Hello {name},

Here are the details you entered:

- Name: {name}
- Date of Birth: {dob}
- Mobile Number: {phone}
- Instagram ID: {insta}
- Email: {email}

Thank you!
"""
msg = MIMEMultipart()
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SENDER_EMAIL, SENDER_PASSWORD)
server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
server.quit()
print(" Details sent to Email successfully!")
