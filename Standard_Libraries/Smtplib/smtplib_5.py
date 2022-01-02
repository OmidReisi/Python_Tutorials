import os
import dotenv

import smtplib
from email.message import EmailMessage

# this module allows us to find the format of a given file(pip install python-magic, pip install python-magic-bin)
import magic


env_file = dotenv.find_dotenv(r"mail.env", raise_error_if_not_found=True)
dotenv.load_dotenv(env_file)

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

email_msg = EmailMessage()

email_msg["Subject"] = "Testing Attachment"
email_msg["From"] = EMAIL_ADDRESS
email_msg["To"] = EMAIL_ADDRESS
email_msg.set_content("This is a test email for attaching files.")

files = [
    r"./Original_Images/image_1.jpg",
    r"./Original_Images/image_2.jpg",
    r"./files/karafarini.pdf",
]


for file in files:

    with open(file, mode="rb") as f:

        file_data = f.read()

        # this method returns the type of the given file in readable human form(if mime = True returns a sting of "maintype/subtype")
        file_maintype, file_subtype = magic.from_file(file, mime=True).split("/")

        email_msg.add_attachment(
            file_data,
            filename=os.path.basename(file),
            maintype=file_maintype,
            subtype=file_subtype,
        )


with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(email_msg)
