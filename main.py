import psutil
import datetime
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
password = os.getenv("APP_PASSWORD")

cpu_usage = psutil.cpu_percent(1)

mem_usage = float(psutil.virtual_memory().percent)

disk_usage = float(psutil.disk_usage("/").percent)

today_date = datetime.datetime.now()
date_var = today_date.strftime("%d-%m-%Y")
time_var = today_date.strftime("%H:%M:%S")

with open("system-monitoring.txt",'w') as f:
    f.write(f"System Analysis on: {date_var} at {time_var}\n\n")
    f.write(f"CPU usage: {cpu_usage}%\n")
    f.write(f"Memory usage: {mem_usage}%\n")
    f.write(f"Disk usage: {disk_usage}%")

def send_email(sender_email,password,receiver_email):
    subject = f"System Report generated on {date_var}"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    body = """
<html>
<body>
<h2>Alert System Analysis</h2>
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

send_email(sender_email,password,receiver_email)
time.sleep(5)
os.remove("system-monitoring.txt")