__author__ = 'alexandre'

# This file will send an email counting graphical stats of the logs
# on a daily basis for example

import smtplib
import credentials


msg = 'Daily monitoring report'

# Credentials are loaded from credentials.py (in the .gitignore file)

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(credentials.username, credentials.password)
server.sendmail(credentials.fromaddr, credentials.toaddrs, msg)
server.quit()