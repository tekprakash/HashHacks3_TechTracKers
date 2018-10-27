import smtplib
import base64
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("sender_email_id","sender_email_password")

def send(message):
    if(message):
        s.sendmail("sender_email_id","receiver_email_id",message)
        s.quit()
    else:
        message = "Sorry"
        s.sendmail("sender_email_id","receiver_email_id",message)
        s.quit()
