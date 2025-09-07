import psutil
import datetime
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# These 2 lines are for local environment with .env file
# from dotenv import load_dotenv
# load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
password = os.getenv("APP_PASSWORD")

cpu_usage = int(psutil.cpu_percent(1))

mem_usage = int(psutil.virtual_memory().percent)

disk_usage = int(psutil.disk_usage("/").percent)

today_date = datetime.datetime.now()
date_var = today_date.strftime("%d-%m-%Y")
time_var = today_date.strftime("%H:%M:%S")

# This block of code will be used to send email
def send_email(sender_email,password,receiver_email):

    with open("system-monitoring.txt",'w') as f:
        f.write(f"System Analysis on: {date_var} at {time_var}\n\n")
        f.write(f"CPU usage: {cpu_usage}%\n")
        f.write(f"Memory usage: {mem_usage}%\n")
        f.write(f"Disk usage: {disk_usage}%")

    subject = f"System Report generated on {date_var}"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    body = """
<html>
<body>
<h2>Alert System Analysis</h2>
<h3>Script initiated by Jenkins pipeline</h3>
<p>Check the attached documents</p>
</body>
</html>
"""
    path_to_file = 'system-monitoring.txt'

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    body_part = MIMEText(body,"html")
    msg.attach(body_part)

    with open(path_to_file, 'r') as file:
        part = MIMEText(file.read(), "plain")
        part.add_header("Content-Disposition", "attachment", filename=os.path.basename(path_to_file))
        msg.attach(part)

    with smtplib.SMTP(smtp_server,smtp_port) as server:
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        print("Email sent successfully")

# This block of code will send the email when memory usage is high triggered by check_resources()
def memory_alert(sender_email,password,receiver_email):
    msg = MIMEMultipart()
    msg["Subject"] = f"Alert! Memory usage is high: {mem_usage}"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    body = """
<html>
<head>
<body>
<h1>Urgent Alert!</h1>
<h3>Memory usage is high, Free the resource</h3>
</body>
</html>
"""
    msg.attach(MIMEText(body,"html"))
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        print("Email sent successfully on memory alert")

# This block of code will send the email when cpu usage is high triggered by check_resources()
def cpu_alert(sender_email,password,receiver_email):
    msg = MIMEMultipart()
    msg["Subject"] = f"Alert! CPU usage is high: {cpu_usage}"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    body = """
<html>
<head>
<body>
<h1>Urgent Alert!</h1>
<h3>CPU usage is high, Check the running processes</h3>
</body>
</html>
"""
    msg.attach(MIMEText(body,"html"))
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        print("Email sent successfully on cpu alert")

# This block of code will send the email when disk usage is high triggered by check_resources()
def disk_alert(sender_email,password,receiver_email):
    msg = MIMEMultipart()
    msg["Subject"] = f"Alert! Disk usage is high: {disk_usage}"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    body = """
<html>
<head>
<body>
<h1>Urgent Alert!</h1>
<h3>Disk usage is high, Free some space...!!</h3>
</body>
</html>
"""
    msg.attach(MIMEText(body,"html"))
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        print("Email sent successfully on disk alert")

# This block of code check resources
def check_resources():

    alert_sent = False

    if cpu_usage > 75:
        cpu_alert(sender_email,password,receiver_email)
        alert_sent = True
    if mem_usage > 75:
        memory_alert(sender_email,password,receiver_email)
        alert_sent = True
    if disk_usage > 80:
        disk_alert(sender_email,password,receiver_email)
        alert_sent = True
    if not alert_sent:
        send_email(sender_email,password,receiver_email)
        # time.sleep(5)
        os.remove("system-monitoring.txt")

check_resources()