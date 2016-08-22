# ---------------------------------------------------------
# Sends a temporary signal to a GPIO pin in a Raspberry Pi
# ---------------------------------------------------------
import RPi.GPIO as GPIO
import time

pin = 7                    # Raspberry Pi's pin 7
delay = 0.25               # Delay in seconds

# Init GPIO
GPIO.setmode(GPIO.BOARD)    
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, 1)        # Set pin to high
time.sleep(delay)          # Wait some milliseconds
GPIO.output(pin, 0)        # Set pin to low
