# services/email_service.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.settings import Config


class EmailService:
    def __init__(self):
        self.email = Config.EMAIL_FROM
        self.password = Config.EMAIL_PASSWORD
        self.smtp_server = Config.SMTP_SERVER
        self.smtp_port = Config.SMTP_PORT

    def send_email(self, recipient_name, subject, body):
        try:
            recipient_name = recipient_name.lower()
            if recipient_name not in Config.EMAIL_CONTACTS:
                return f"No email address found for {recipient_name}"
                
            to_address = Config.EMAIL_CONTACTS[recipient_name]
            
            msg = MIMEMultipart()
            msg["From"] = self.email
            msg["To"] = to_address
            msg["Subject"] = subject

            msg.attach(MIMEText(body, "plain"))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(msg)
            server.quit()

            return f"Email sent successfully to {recipient_name} ({to_address})"
        except Exception as e:
            return f"Failed to send email: {str(e)}"