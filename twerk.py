# MANSEDS Antdroid - Main control file
# Author: Ethan Ramsay

# Import Dependencies
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from TwitterAPI import TwitterAPI

# Setup GPIO
GPIO.setmode(GPIO.BCM)

# Setup pins
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
servo = GPIO.PWM(18, 50)

# Stop function
def stop(pin):
    GPIO.cleanup()
    take_photo()

# Add event detection
GPIO.add_event_detect(17, GPIO.FALLING, callback=stop)

# Set up twitter
CONSUMER_KEY = 'gbn2RKsVY9duPSo30bKxMOGqt'
CONSUMER_SECRET = 'OKsXRAms9j7ReK9kNEsHPiFz4Ym0p1l8De3ZEgpbmLZ0O5ETrI'
ACCESS_TOKEN_KEY = '990337143531888640-sOb1gkYlQ4cNFJNoy7AbPrcjlEX35jB'
ACCESS_TOKEN_SECRET = 'Iq2rBjbqyUCletFiFpWf2ImvqrbUMNOnaJCkQ4xPVERib'

# Tweet photo
def tweet_photo(photo_filename):
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    file = open(photo_filename, 'rb')
    data = file.read()
    r = api.request('statuses/update_with_media', {'status':'Antdroid checking in'}, {'media[]':data})
    print(r.status_code)

# Setup camera
camera = PiCamera()
camera.resolution(2592, 1944)
camera.annotate_text = ("Antdroid phone home")

# Take photo
def take_photo():
    camera.start_preview()
    time.sleep(2)
    filename = '/image-capture/'+str(datetime.datetime.now())+'.jpg'
    camera.capture(filename)
    camera.stop_preview()
    tweet_photo(filename)

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
take_photo()
GPIO.cleanup()
