import os
import dotenv
import io
import smtplib
from email.message import EmailMessage
from PIL import Image


env_file = dotenv.find_dotenv(r"mail.env", raise_error_if_not_found=True)
dotenv.load_dotenv(env_file)

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

email_msg = EmailMessage()

email_msg["Subject"] = "This Terms Final Exams"
email_msg["From"] = EMAIL_ADDRESS
email_msg["To"] = EMAIL_ADDRESS
email_msg.set_content("Remember that final exams start on January 2")

img = Image.open(r"./Original_Images/image_1.jpg")

img_bytes = io.BytesIO()
# if you're saving an image on bytes array object you have to pass in the format
img.save(img_bytes, format=img.format)
# turning a byte array object to bytes
img_bytes = img_bytes.getvalue()
# if the PIl.Image object is opend using a path to an existing file then the img object has the filename attribute
# but if it's created using bytes or anything other than path to existing file then it doesn't have filename attribute and the following line raises an error
file_name = os.path.basename(img.filename)

# the add attachment method takes the following argument
# first argument is the content of your file in bytes (this value should be passed as positional argument and not keyword argument)
# you can't use img.tobytes() method to pass your data because it's raw bytes and image becomes corrupted
# you can use the following way for your data or open the image file normaly in "rb" mode and use f.read() to get the data bytes
# maintype and subtype are the mime_types based on your file extension (mime_type = maintype/subtype)
# you can find all mime_types in the following link
# https://docs.w3cub.com/http/basics_of_http/mime_types/complete_list_of_mime_types
# filename is the filename you want to set for your file in the email
email_msg.add_attachment(
    img_bytes,
    filename=file_name,
    maintype="image",
    subtype=img.format.lower(),
)


with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465) as smtp:
    smtp.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
    smtp.send_message(email_msg)
