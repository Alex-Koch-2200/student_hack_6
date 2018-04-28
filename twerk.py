# MANSEDS Antdroid - Main control file
# Author: Ethan Ramsay

# Import Dependencies
import RPi.GPIO as GPIO
import time
from picamera import PiCamera

# Setup GPIO
GPIO.setmode(GPIO.BCM)

# Setup pins
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
servo = GPIO.PWM(18, 50)

# Stop function
def stop(pin):
    GPIO.cleanup()
    camera.start_preview()
    time.sleep(2)
    camera.capture('/image-capture/stopped-'+str(datetime.datetime.now())+'.jpg')
    camera.stop_preview()  

# Add event detection
GPIO.add_event_detect(17, GPIO.FALLING, callback=stop)

# Setup camera
camera = PiCamera()
camera.resolution(2592, 1944)
camera.annotate_text = ("Antdroid phone home")

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
camera.start_preview()
time.sleep(2)
camera.capture('/image-capture/'+str(datetime.datetime.now())+'.jpg')
camera.stop_preview()
GPIO.cleanup()
