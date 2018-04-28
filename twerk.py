# Import Dependencies
import RPi.GPIO as GPIO
import time

# Setup GPIO
GPIO.setmode(GPIO.BCM)

# Setup pins
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
servo = GPIO.PWM(18, 50)

# Stop function
def stop(pin):
    GPIO.cleanup()

# Add event detection
GPIO.add_event_detect(17, GPIO.FALLING, callback=stop)


# Twerk
var = True
for i in range(50):
    if var:
        servo.start(6)
        var = False
    else:
        servo.start(8)
        var = True
    time.sleep(0.1)

servo.start(7)
time.sleep(0.3)
GPIO.cleanup()
