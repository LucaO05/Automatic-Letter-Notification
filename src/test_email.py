from email_service import EmailService
from config import Config

if __name__ == "__main__":
    email_service = EmailService(
        Config.smtp_server,
        Config.smtp_port,
        Config.sender_Email,
        Config.sender_Password,
        Config.recipient_Email
    )
    
    email_service.send_email()
