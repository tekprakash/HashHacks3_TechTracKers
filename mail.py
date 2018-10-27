import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login("sender_email_id", "sender_email_password")


message = "I am at HashHacks"

s.sendmail("sender_email_id", "receiver_email_id", message)

s.quit()

#Here we can use base64 for encrypting passwords
                
