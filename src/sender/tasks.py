import smtplib

from celery_worker import celery_app
from config import SMTP_PASS, SMTP_USER, SMTP_HOST, SMTP_PORT
from sender.services import get_email_template_dashboard


@celery_app.task
def send_email_report_dashboard(user_email: str):
    email_template = get_email_template_dashboard(user_email)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(email_template)
