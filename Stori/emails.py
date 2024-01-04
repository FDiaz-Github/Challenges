import os
import smtplib
import settings
import base64
from jinja2 import Environment, FileSystemLoader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
email_ps = os.environ.get('EMAIL_PASSWORD')


def generate_email_content(summary):
    """
    Using the template email_template, this function generates the email using
    the transaction summary

    :param summary:
    :return: email with summary data
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    resources_dir = os.path.join(current_dir, 'resources')
    env = Environment(loader=FileSystemLoader(resources_dir))
    template = env.get_template('email_template.html')
    return template.render(summary)


def send_email(subject, body) -> None:
    msg = MIMEMultipart()
    msg['From'] = settings.EMAIL_SENDER
    msg['To'] = settings.EMAIL_RECEIVER
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)  # Change to your SMTP server
    server.starttls()
    server.login(settings.EMAIL_SENDER, email_ps)
    server.send_message(msg)
    server.quit()
