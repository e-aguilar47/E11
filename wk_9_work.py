import RPi.GPIO as GPIO
import time

counts=0

def my_callback(channel):
   print(f"Count detected at{time.time()}")

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.add_event_detect(26, GPIO.FALLING, callback=my_callback)

while True:
   time.sleep(10)
   print(f"Number of counts measured is {counts}")
 
