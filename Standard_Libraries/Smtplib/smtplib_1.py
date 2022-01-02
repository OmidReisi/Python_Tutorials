# in order to send emails you need to enable 2-step verification for your mail account
# then you need to generate a new password in app passwords for your usecase
# store the generated password in an .env file

import smtplib
import os
import dotenv

env_file = dotenv.find_dotenv(filename=r"mail.env", raise_error_if_not_found=True)
dotenv.load_dotenv(env_file)

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

# use context managers with smtplib in order to make sure the connection is closed when you're finished
# host is your mail host (for gmail we use smtp.gmail.com)
# for plain SMTP port number is 587
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:

    # this method identifies us with the mail server
    smtp.ehlo()

    # puts the connection in TLS mode and encrypts it
    smtp.starttls()

    # after encrypting we need to identify ourself again
    smtp.ehlo()

    # log in to your mail account
    # if the 2-step verification is enabled for your account then the password is the generated app password key
    smtp.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)

    subject = "smtplib_1: Grab dinner this weekend?"
    body = "How about dinner at 6pm this Saturday?"

    # if you use plain text in constructing your email then you need to add subject as your header and then at least 2 blank lines and then your body
    msg = f"Subject: {subject}\n\n{body}"

    # to send the email first argument is the sender(the email address we logged in with), second one is the reciever(reciever can be same as the sendor so we send the email to ourself) and then the msg
    smtp.sendmail(from_addr=EMAIL_ADDRESS, to_addrs="omid79.dg@gmail.com", msg=msg)
