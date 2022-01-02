import smtplib

# this class from this module is used for giving structure to our email message
from email.message import EmailMessage

import os
import dotenv

env_file = dotenv.find_dotenv(filename=r"mail.env", raise_error_if_not_found=True)
dotenv.load_dotenv(env_file)

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

# we set our email to an instance of this class
email = EmailMessage()

# this is how we set our email details
# notice the keys start with capital letters
email["Subject"] = "smtplib_3: Grab dinner this weekend?"

# if you want to send the email to multiple accounts just seperate them with ", "
# remember this has to be a string and don't use list for multiple recepients
email["From"] = EMAIL_ADDRESS
email["To"] = EMAIL_ADDRESS

# this is how we set the body of our email (body of our message)
email.set_content("How about dinner at 6pm this Saturday?")

# using SMTP_SSL class instead of SMTP uses an SSL concetion from the begining which is encrypted and you don't need to use ehlo() and starttls() methods anymore
# the port number for SMTP_SSL is 465
with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as smtp:

    smtp.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
    # now that we have created our email object we use send_message instead of sendmail
    smtp.send_message(email)
