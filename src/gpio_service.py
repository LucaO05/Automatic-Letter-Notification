import RPi.GPIO as gpio

class GPIOService:
    def __init__(self, sensorPin, lampPin, switch):
        self.sensor_pin = sensorPin
        self.lamp_pin = lampPin
        self.switch_pin = switch
        
    def setup(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(self.sensor_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        gpio.setup(self.lamp_pin, gpio.OUT)
        gpio.setup(self.switch_pin, gpio.IN, pull_up_down=gpio.PUD_UP)
        
    def add_event_detect(self):
        gpio.add_event_detect(self.sensor_pin, gpio.RISING, callback=self.post_received, bouncetime=300)
        gpio.add_event_detect(self.switch_pin, gpio.FALLING, callback=self.lamp_down, bouncetime=300)

    def post_received(self, channel):
        gpio.output(self.lamp_pin, gpio.HIGH)
        email_service.send_email()
        
    def lamp_down(self, channel):
        gpio.output(self.lamp_pin, gpio.LOW)
        
    def cleanup(self):
        gpio.cleanup()