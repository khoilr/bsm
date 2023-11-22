from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from server.report.report import generateReport
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import schedule
import time


def send_email(
    sender_email,
    sender_password,
    receiver_email,
    subject,
    html_template_path,
    attachment_path=None,
):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Read HTML template file
    with open(html_template_path, "r") as file:
        html_content = file.read()

    # Attach HTML content to the email
    html_body = MIMEText(html_content, "html")
    message.attach(html_body)

    # Attach file if provided
    if attachment_path:
        try:
            with open(attachment_path, "rb") as file:
                attachment = MIMEApplication(
                    file.read(), _subtype="xlsx"
                )  # Change the subtype based on the file type
                attachment.add_header(
                    "Content-Disposition", "attachment", filename=attachment_path.replace("server/report/", "")
                )
                message.attach(attachment)
        except:
            ### insert data
            generateReport()
            with open(attachment_path, "rb") as file:
                attachment = MIMEApplication(
                    file.read(), _subtype="xlsx"
                )  # Change the subtype based on the file type
                attachment.add_header(
                    "Content-Disposition", "attachment", filename=attachment_path.replace("server/report/", "")
                )
                message.attach(attachment)


    # Connect to the SMTP server (in this case, Google's SMTP server)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully!")


def job():
    # Set your email and scheduling details
    sender_email = "Indofa1804@gmail.com"
    sender_password = "qybwkivbwkyncdlv"
    # replace with anh Long's email
    receiver_email = "vinhpna@1cinnovation.com"
    subject = f"Daily Check-In Report {datetime.now().strftime('%d_%m_%Y')}"
    html_template_path = "template.html"
    attachment_path = f"server/report/Report_{datetime.now().strftime('%d_%m_%Y')}.xlsx"

    send_time = ["15:34"]

    current_time = time.strftime("%H:%M")

    if current_time in send_time:
        send_email(
            sender_email,
            sender_password,
            receiver_email,
            subject,
            html_template_path,
            attachment_path,
        )


def schedule_mail():
    schedule.every().minute.at(":00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

schedule_mail()
# class ScheduleManager:
#     _schedule = BlockingScheduler()
#     _jobs = []

#     def __init__(self):
#         pass

#     def addNewJob(self, func, scheduleTime: datetime, args: list[str] = []):
#         self._jobs.append(
#             {
#                 "function": func,
#                 "args": args,
#                 "time": scheduleTime,
#             }
#         )

#     def start(self):
#         for job in self._jobs:
#             self._schedule.add_job(
#                 func=job["function"],
#                 trigger="date",
#                 run_date=job["time"],
#                 args=job["args"],
#             )
#         self._schedule.start()
