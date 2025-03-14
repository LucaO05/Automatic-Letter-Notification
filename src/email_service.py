import smtplib
from email.mime.text import MIMEText

class EmailService:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password, recipient_email):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
    
    def send_email(self):
        msg = MIMEText("Es ist Post eingegangen")
        msg["Subject"] = "Es ist Post im Briefkasten"
        msg["From"] = self.sender_email
        msg["To"] = self.recipient_email
        
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
                print("E-Mail gesendet")
        except Exception as e:
            print(f"Fehler beim Senden: {e}")
