# if you want to test sending emails you should use a debug mail server on the localhost with the following command in a terminal
# python -m aiosmtpd -n -l localhost:1025 (you should have aiosmtpd module installed)
# this command sets up  localhost on selected port  for SMTP connections
# the port number is better to larger than 1024 (port > 1024) in order to make sure it's empty
# python -m aiosmtpd -n (this is the shortcut for setting up localhost:8025)
# now when we send an email it prints it in the terminal
# remember that we don't need anymore logging and no more encrypting

import smtplib

# now our SMTP connection is on localhost with port 8025
with smtplib.SMTP(host="localhost", port=1025) as smtp:

    subject = "smtplib_2: Grab dinner this weekend?"
    body = "How about dinner at 6pm this Saturday?"

    msg = f"Subject: {subject}\n\n{body}"

    # now that you're sending the mail to a debug server and printing it to stdout you don't need any sender and reciever and you pass them as empty strings(the sendor and receiver are ignored and doesn't matter what they are in this situation)
    smtp.sendmail("", "", msg=msg)
