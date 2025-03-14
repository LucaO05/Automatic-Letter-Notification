from gpio_service import GPIOService
from email_service import EmailService
from config import Config

def main():
    email_service = EmailService(Config.smpt_Server, Config.smpt_port, Config.sender_Email, Config.sender_Password, Config.recipient_Email)
    gpio_service = GPIOService(Config.sensorPin, Config.lampPin, Config.switch, email_service)
    
    try: 
        gpio_service.setup()
        gpio_service.add_event_detect()
        while True:
            pass
    except KeyboardInterrupt:
        print("\nBeende Programm...")
    except Exception as e:
        print(f"Fehler: {e}")
    finally:
        gpio_service.cleanup()
        
if __name__ == "__main__":
    main()   