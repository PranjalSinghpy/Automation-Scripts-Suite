import getpass
import smtplib

Host = "smtp.gmail.com"
Port = 587 

From_Email = "pranjalsingj75@gmail.com"
To_Email = "shushyyy.23@gmail.com"

# Yaha actual Gmail password nahi, APP PASSWORD use hoga
Password = getpass.getpass("Enter App Password: ")

Message = """Subject: Mail sent using python

Hi allaboutpython,
this email is sent using a test account.

Thanks,
Test Account
"""

smtp = smtplib.SMTP(Host, Port)
print(smtp.ehlo())

print(smtp.starttls())

print(smtp.login(From_Email, Password))

smtp.sendmail(From_Email, To_Email, Message)
smtp.quit()
