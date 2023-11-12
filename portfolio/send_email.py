import os
import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = os.environ("SENDER")
    reciever = os.environ("RECIEVER")
    password = os.environ("PASSWORD")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)

if __name__ == "__main__":
    msg = """\
Subject: Streamlit. Test message
Test message Python smtplib"""
    send_email(msg)
