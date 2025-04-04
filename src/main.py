from gpio_service import GPIOService
from email_service import EmailService
from config import Config
import time

def main():
    print("Starting Mailbox Notification System...")
    
    # Initialize services
    print("Initializing email service...")
    email_service = EmailService(Config.smtp_server, Config.smtp_port, Config.sender_Email, Config.sender_Password, Config.recipient_Email)
    
    print("Initializing GPIO service...")
    gpio_service = GPIOService(Config.sensorPin)
    gpio_service.email_service = email_service
    
    try:
        print("Setting up GPIO pins...")
        gpio_service.setup()
        
        print("Adding event detection...")
        gpio_service.add_event_detect()
        
        print("System ready! Waiting for mail...")
        # Use a more controlled loop with a short sleep
        while True:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"Error in main program: {e}")
    finally:
        print("Cleaning up resources...")
        gpio_service.cleanup()
        print("Program ended.")
        
if __name__ == "__main__":
    main()
