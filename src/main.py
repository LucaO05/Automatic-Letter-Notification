from gpio_service import GPIOService
from email_service import EmailService
from config import Config
import time
import RPi.GPIO as gpio

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
        
        # Try to add event detection
        use_interrupts = gpio_service.add_event_detect()
        
        if use_interrupts:
            print("Using interrupt-based detection. System ready!")
            # Main loop with interrupts
            while True:
                time.sleep(0.1)
        else:
            print("Using polling-based detection instead. System ready!")
            # Polling approach as fallback
            prev_state = gpio.input(Config.sensorPin)
            mail_detected = False
            
            while True:
                current_state = gpio.input(Config.sensorPin)
                
                # Detect rising edge (0 to 1)
                if current_state == 1 and prev_state == 0:
                    print("Mail detected via polling!")
                    if not mail_detected:
                        mail_detected = True
                        email_service.send_email()
                elif current_state == 0 and mail_detected:
                    # Reset detection state when sensor returns to 0
                    mail_detected = False
                
                prev_state = current_state
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
