import RPi.GPIO as gpio
import time

class GPIOService:
    def __init__(self, sensorPin, lampPin, switch):
        self.sensor_pin = sensorPin
        self.lamp_pin = lampPin
        self.switch_pin = switch
        self.email_service = None  # This will be set in main.py
        
    def setup(self):
        # Clean up any previous GPIO setups to avoid conflicts
        gpio.cleanup()
        
        # Set mode and configure pins
        gpio.setmode(gpio.BCM)
        gpio.setup(self.sensor_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        gpio.setup(self.lamp_pin, gpio.OUT)
        gpio.setup(self.switch_pin, gpio.IN, pull_up_down=gpio.PUD_UP)
        
        # Initialize lamp state
        gpio.output(self.lamp_pin, gpio.LOW)
        
        # Allow system time to stabilize
        time.sleep(0.5)
        
    def add_event_detect(self):
        try:
            # Remove any existing event detection first
            try:
                gpio.remove_event_detect(self.sensor_pin)
                gpio.remove_event_detect(self.switch_pin)
            except:
                pass  # If there was no event detection, continue
                
            # Add event detection with error handling
            gpio.add_event_detect(self.sensor_pin, gpio.RISING, callback=self.post_received, bouncetime=300)
            print(f"Successfully added event detection to sensor pin {self.sensor_pin}")
            
            gpio.add_event_detect(self.switch_pin, gpio.FALLING, callback=self.lamp_down, bouncetime=300)
            print(f"Successfully added event detection to switch pin {self.switch_pin}")
            
        except Exception as e:
            print(f"Error setting up event detection: {e}")
            raise  # Re-raise the exception to be caught in main

    def post_received(self, channel):
        print(f"Post detected on pin {channel}!")
        gpio.output(self.lamp_pin, gpio.HIGH)
        if self.email_service:
            print("Sending email notification...")
            self.email_service.send_email()
        else:
            print("Warning: No email service configured")
        
    def lamp_down(self, channel):
        print(f"Switch pressed on pin {channel}, turning lamp off")
        gpio.output(self.lamp_pin, gpio.LOW)
        
    def cleanup(self):
        print("Cleaning up GPIO")
        gpio.cleanup()
