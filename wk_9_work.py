import RPi.GPIO as GPIO
import time
import sys
import csv

counts=0
start_time=time.time()
run_time=int(sys.argv[1])

filename='data.csv'
filename=sys.argv[2]
file=open(filename,'w',newline='')
writer=csv.writer(file)

def my_callback(channel):
   print(f"Count detected at{time.time()}")

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.add_event_detect(26, GPIO.FALLING, callback=my_callback)

now=time.time()
while (now-start_time)<run_time:
   time.sleep(10)
   print(f"Number of counts measured is {counts}")
 