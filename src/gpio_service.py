import RPi.GPIO as gpio
import time

class GPIOService:
    def __init__(self, sensorPin):
        self.sensor_pin = sensorPin
        self.email_service = None
        
    def setup(self):
        print(f"Setting up GPIO for sensor pin {self.sensor_pin}")
        
        # Clean up any previous configurations
        try:
            gpio.cleanup()
        except:
            print("Note: No cleanup needed")
        
        # Set the GPIO mode
        gpio.setmode(gpio.BCM)
        print("GPIO mode set to BCM")
        
        # Configure the sensor pin with pull-down resistor
        gpio.setup(self.sensor_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        print(f"Pin {self.sensor_pin} set as INPUT with pull-down")
        
        # Test reading from the pin
        current_state = gpio.input(self.sensor_pin)
        print(f"Current state of pin {self.sensor_pin}: {current_state}")
        
        # Give system time to stabilize
        time.sleep(1)
        
    def add_event_detect(self):
        print(f"Attempting to add event detection for pin {self.sensor_pin}")
        
        # Try different approach to event detection
        try:
            # First check if we can remove existing detection
            try:
                print("Removing any existing event detection...")
                gpio.remove_event_detect(self.sensor_pin)
            except Exception as e:
                print(f"No existing detection to remove: {e}")
                
            # Try with wait time between operations
            time.sleep(0.5)
            
            # Add event detection with less sensitivity
            print("Adding event detection...")
            gpio.add_event_detect(self.sensor_pin, gpio.RISING, callback=self.post_received, bouncetime=500)
            print(f"Successfully added event detection to sensor pin {self.sensor_pin}")
            
        except Exception as e:
            print(f"Error setting up event detection: {e}")
            print("Trying alternative approach...")
            
            # Alternative approach: polling instead of interrupt
            print("Setting up polling method instead of interrupts")
            return False
            
        return True

    def post_received(self, channel):
        print(f"Post detected on pin {channel}!")
        if self.email_service:
            print("Sending email notification...")
            self.email_service.send_email()
        else:
            print("Warning: No email service configured")
        
    def cleanup(self):
        print("Cleaning up GPIO resources")
        try:
            gpio.cleanup()
            print("GPIO cleanup successful")
        except Exception as e:
            print(f"GPIO cleanup error: {e}")
