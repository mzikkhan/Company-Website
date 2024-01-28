import smtplib, ssl
import os

def send_email(mesg):
    host = "smtp.gmail.com"
    port = 465

    password = os.getenv("PASSWORD")
    username = "edrenaline0@gmail.com"

    receiver = "mohammad.khan06@northsouth.edu"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, mesg)


